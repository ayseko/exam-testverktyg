from behave import given, when, then
from playwright.sync_api import expect


@given('att användaren navigerar till katalogen')
def step_navigate_to_catalog(context):
    context.page.goto(context.base_url)


@then("ska böckerna visas i katalogen")
def step_verify_books_visible(context):
    star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(star).to_be_visible()


@when('användaren klickar på hjärtat för den första boken')
def step_click_first_star(context):
    first_star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    first_star.click()


@then('ska boken markeras som favorit')
def step_verify_book_is_favorite(context):
    first_star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(first_star).to_have_class("star selected")


@given('att användaren har favoritmarkerat en bok i katalogen')
def step_setup_favorite_book(context):
    context.page.goto(context.base_url)
    first_star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    first_star.click()


@when('användaren klickar på hjärtat för boken igen')
def step_click_star_again(context):
    first_star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    first_star.click()


@then("ska favoritmarkeringen tas bort")
def step_verify_favorite_removed(context):
    first_star = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(first_star).to_have_class("star")