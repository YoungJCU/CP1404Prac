import wikipedia

from wikipedia.exceptions import DisambiguationError, PageError

def main():
    print("Enter page title (empty input to quit):")
    user_input = input("Enter page title: ").strip()

    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
            print()
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])
            print()
        except PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')
            print()
        user_input = input("Enter page title: ").strip()
    print("Thank you.")

if __name__ == "__main__":
    main()
