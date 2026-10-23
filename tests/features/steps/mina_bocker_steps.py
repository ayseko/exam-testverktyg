from behave import when, then
from playwright.sync_api import expect


@when('användaren navigerar till "{tab_name}"')
def step_navigate_to_tab(context, tab_name):
    context.page.get_by_role("button", name=tab_name).click()


@then('ska den favoritmarkerade boken visas i listan')
def step_verify_favorite_book_visible(context):
    favorite_item = context.page.get_by_test_id("book-list").get_by_role("listitem").first
    expect(favorite_item).to_be_visible()


@then('ska boken inte längre visas i listan')
def step_verify_favorite_removed_from_my_books(context):
    items = context.page.get_by_test_id("book-list").get_by_role("listitem")
    expect(items).to_have_count(0)