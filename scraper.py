import requests

from bs4 import BeautifulSoup


# ? FUNCTION DEFINITIONS:

# Prints a integer value on how many instances of the [citation needed]
# tag are present on the page. skips over the larger, section-wide
# "This page needs additional citations" element.
def get_citations_needed_count(url):

    r = requests.get(url)

    markup = r.text
    # Feed into Beautiful Soup to parse into HTML
    soup = BeautifulSoup(markup, "html.parser")

    # Select and save only instances of the [citation needed] superscript to a list
    instances = soup.select("sup.noprint.Inline-Template.Template-Fact")

    # print the number of entries in our list
    print(f"There are {len(instances)} citations needed on this page.")
    return len(instances)


# Prints the full contents of the <p> tag containing the [citation needed],
# for reference on what topic is uncited.
def get_citations_needed_report(url):

    r = requests.get(url)

    markup = r.text

    # Create instances list, and set phrase we are searching for to "citation needed"
    instances = []
    target_phrase = "citation needed"

    # Feed into Beautiful Soup to parse into HTML
    soup = BeautifulSoup(markup, "html.parser")

    # get all p tags present in page
    for p_tags in soup.find_all("p"):

        # iterate through all p tags and save the ones with target phrase
        if target_phrase in p_tags.get_text():

            instances.append(p_tags.get_text())

    # Print each entry of list individually
    for i in range(len(instances)):
        print(instances[i])
        print()


# ? MAIN
if __name__ == "__main__":

    url = input("please paste in the url to get a citation count of ")

    r = requests.get(url)

    markup = r.text

    get_citations_needed_count(url)

    # Prompt user if they want the report as well, if Y or y input, do so.
    if input("would you like a report as well? Y/N ").lower() == "y":
        print()
        get_citations_needed_report(url)
