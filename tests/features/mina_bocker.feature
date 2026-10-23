Feature: Mina böcker

  Scenario: Visa favoritmärkta böcker i Mina böcker
    Given att användaren navigerar till katalogen
    When användaren klickar på hjärtat för den första boken
    And användaren navigerar till "Mina böcker"
    Then ska den favoritmarkerade boken visas i listan

  Scenario: Ta bort en bok från favoriter och verifiera i Mina böcker
    Given att användaren navigerar till katalogen
    When användaren klickar på hjärtat för den första boken
    And användaren navigerar till "Mina böcker"
    Then ska den favoritmarkerade boken visas i listan
    When användaren navigerar till "Katalog"
    And användaren klickar på hjärtat för den första boken
    And användaren navigerar till "Mina böcker"
    Then ska boken inte längre visas i listan