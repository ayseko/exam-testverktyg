
Feature: Katalog

  Scenario: Visa böcker i katalogen
    Given att användaren navigerar till katalogen
    Then ska böckerna visas i katalogen

  Scenario: Favoritmarkera en bok i katalogen
    Given att användaren navigerar till katalogen
    When användaren klickar på hjärtat för den första boken
    Then ska boken markeras som favorit

  Scenario: Ta bort favoritmarkering i katalogen
    Given att användaren har favoritmarkerat en bok i katalogen
    When användaren klickar på hjärtat för boken igen
    Then ska favoritmarkeringen tas bort
