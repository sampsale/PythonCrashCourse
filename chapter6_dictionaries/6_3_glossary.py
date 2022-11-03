glossary = {
    'for_loop': 'loops through list',
    'conditional': 'checks if something is true',
    'list': 'list of objects',
    'tuple': 'immutable list',
    'dictionary': 'stores data in key-value pairs'
}

for concept, meaning in glossary.items():
    print(f"\tConcept: {concept.title()} Meaning: {meaning.capitalize()}")