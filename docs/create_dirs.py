import os
import yaml

def create_directories(directories):
    for categories in directories:
        for category in categories.keys():
            category_path = "prompts/"+category.replace(' ', '_')
            os.makedirs(category_path, exist_ok=True)
            for subcategory in categories[category]:
                subcategory_path = os.path.join(category_path, subcategory.replace(' ', '_'))
                if not os.path.exists(subcategory_path) or not os.listdir(subcategory_path):
                    subcategory_path = subcategory_path+"/_posts"
                    os.makedirs(subcategory_path)
                    readme_path = os.path.join(subcategory_path, 'README.md')
                    with open(readme_path, 'w') as f:
                        f.write('# {} - {}\n\nThis directory contains prompts related to {}.'.format(category, subcategory, subcategory))


with open('categories.yml', 'r') as f:
    directories = yaml.safe_load(f)
    create_directories(directories)