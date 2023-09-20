import wikipedia

page_title = input("Enter a page title (blank to exit): ").strip()
while page_title != "":

    try:
        wikipedia_page = wikipedia.page(title=page_title, auto_suggest=False)

        print("Title:", wikipedia_page.title)
        print("Summary:", wikipedia_page.summary)
        print("URL:", wikipedia_page.url)

    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)

    except wikipedia.exceptions.PageError:
        print("Page not found.")

    except Exception as error:
        print("An error occurred:", str(error))

    page_title = input("Enter a page title (blank to exit): ").strip()

print("Goodbye!")
