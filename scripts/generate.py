"""
generate.py - Génère quotidiennement du contenu utile pour ai-interaction-patterns.

Ce script:
1. Choisit un type de contenu aléatoire (prompt, best practice, code example, discussion)
2. Sélectionne un template aléatoire depuis templates.yaml
3. Appelle l'API Claude pour générer du contenu authentique et utile
4. Sauvegarde le fichier dans le bon dossier avec la date du jour

Contenu auto-généré via interaction humain-IA (Claude API).
"""

import os
import random
import yaml
import datetime
import logging
from anthropic import Anthropic

# --- Configuration du logging (pour voir ce qui se passe) ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_templates(path="scripts/templates.yaml"):
    """
    Charge les templates depuis le fichier YAML.
    Chaque template = un sujet/angle différent pour varier le contenu.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def choose_content_type(templates):
    """
    Choisit aléatoirement un type de contenu parmi les catégories disponibles.
    Retourne: (type_name, template_text, output_folder)
    """
    # Mapping: clé YAML -> dossier de sortie
    type_to_folder = {
        "prompt_templates": "prompts",
        "best_practices": "docs",
        "code_examples": "examples",
        "discussions": "discussions"
    }

    # Choisir un type aléatoire
    content_type = random.choice(list(type_to_folder.keys()))
    folder = type_to_folder[content_type]

    # Choisir un template aléatoire dans ce type
    template = random.choice(templates[content_type])

    logger.info(f"Type choisi: {content_type}")
    logger.info(f"Template: {template}")

    return content_type, template, folder


def generate_content(template, content_type):
    """
    Appelle l'API Claude pour générer du contenu basé sur le template.
    Le contenu doit être authentique, utile, et naturel.
    """
    # Initialiser le client Anthropic
    # La clé API est lue depuis la variable d'environnement ANTHROPIC_API_KEY
    client = Anthropic()

    # Instructions pour Claude: générer du contenu naturel et utile
    system_prompt = """You are a practitioner documenting real insights from daily 
human-AI collaboration. Write in a natural, practical voice. Share specific 
experiences, patterns that work, and honest observations.

Guidelines:
- Write 300-500 words
- Be specific and actionable (real examples, not platitudes)
- Natural tone (not corporate, not academic, not preachy)
- Include what works AND what doesn't
- Offer 2-3 approaches when relevant (not just one "right answer")
- Acknowledge tradeoffs honestly
- Format as markdown with clear structure

This content is auto-generated via human-AI interaction for the 
ai-interaction-patterns repository."""

    # Construire le prompt utilisateur
    user_prompt = f"""Write a {content_type.replace('_', ' ')} about:
{template}

Make it genuinely useful for someone working with AI tools daily. 
Draw from practical experience. Be honest about limitations."""

    logger.info("Appel API Claude...")

    # Appel API
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        system=system_prompt
    )

    # Extraire le texte de la réponse
    content = message.content[0].text

    logger.info(f"Contenu généré: {len(content)} caractères")

    return content


def save_content(content, folder, template):
    """
    Sauvegarde le contenu généré dans le bon dossier.
    Nom du fichier: YYYY-MM-DD_description.md
    """
    # Date du jour pour le nom de fichier
    today = datetime.date.today().strftime("%Y-%m-%d")

    # Créer un nom de fichier lisible à partir du template
    # Ex: "Practical prompt for workflow" -> "practical_prompt_for_workflow"
    slug = template.lower()
    slug = slug.replace(" ", "_")
    # Garder seulement lettres, chiffres, underscores
    slug = "".join(c for c in slug if c.isalnum() or c == "_")
    # Limiter la longueur
    slug = slug[:50]

    filename = f"{today}_{slug}.md"
    filepath = os.path.join(folder, filename)

    # Ajouter footer de transparence
    footer = f"""

---
*Auto-generated content via human-AI interaction (Claude API) - {today}*  
*Repository: [ai-interaction-patterns](https://github.com/Mesnildot/ai-interaction-patterns)*
"""
    content_with_footer = content + footer

    # Créer le dossier si nécessaire
    os.makedirs(folder, exist_ok=True)

    # Sauvegarder
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content_with_footer)

    logger.info(f"Fichier sauvegardé: {filepath}")

    return filepath


def main():
    """
    Fonction principale:
    1. Charge templates
    2. Choisit type + template aléatoire
    3. Génère contenu via API
    4. Sauvegarde dans bon dossier
    """
    logger.info("=== Début génération quotidienne ===")

    try:
        # 1. Charger templates
        templates = load_templates()
        logger.info("Templates chargés")

        # 2. Choisir type et template
        content_type, template, folder = choose_content_type(templates)

        # 3. Générer contenu
        content = generate_content(template, content_type)

        # 4. Sauvegarder
        filepath = save_content(content, folder, template)

        logger.info(f"=== Succès! Fichier créé: {filepath} ===")

    except Exception as e:
        logger.error(f"=== Erreur: {e} ===")
        raise


# Point d'entrée: lance main() quand on exécute le script
if __name__ == "__main__":
    main()
