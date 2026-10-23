from behave import given, when, then
from playwright.sync_api import expect


@given('att användaren navigerar till "Lägg till bok"')
def step_navigate_to_add_book(context):
    context.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
    context.page.get_by_role("button", name="Lägg till bok").click()


@when('användaren fyller i författare "{author}" och titel "{title}"')
def step_fill_book_form(context, author, title):
    context.page.get_by_label("Författare").fill(author)
    context.page.get_by_label("Titel").fill(title)


@when('klickar på knappen "Lägg till"')
def step_click_add_button(context):
    context.page.get_by_role("button", name="Lägg till ny bok", exact=True).click()


@then('ska boken "{title}" visas i katalogen')
def step_verify_book_in_catalog(context, title):
    context.page.get_by_role("button", name="Katalog").click()
    expect(context.page.get_by_text(title)).to_be_visible()


@then('ska knappen "Lägg till" vara inaktiverad')
def step_verify_add_button_disabled(context):
    add_button = context.page.get_by_role("button", name="Lägg till ny bok", exact=True)
    expect(add_button).to_be_disabled()