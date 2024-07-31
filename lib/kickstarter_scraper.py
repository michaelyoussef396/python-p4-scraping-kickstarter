from bs4 import BeautifulSoup
import ipdb

# projects: kickstarter.select("li.project.grid_4")[0]
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        projects[title] = {
            'image_link': project.select("div.project-thumbnail a img")[0]['src'],
            'description': project.select("p.bbcard_blurb")[0].text,
            'location': project.select("ul.project-meta span.location-name")[0].text,
            'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")
        }

    # return the projects dictionary
    return projects

# To run and see the results
if __name__ == "__main__":
    projects = create_project_dict()
    for title, details in projects.items():
        print(f"Title: {title}")
        print(f"Image Link: {details['image_link']}")
        print(f"Description: {details['description']}")
        print(f"Location: {details['location']}")
        print(f"Percent Funded: {details['percent_funded']}")
        print("-" * 20)
