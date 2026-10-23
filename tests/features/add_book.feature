Feature: Lägg till bok

  Scenario: Lägga till en ny bok i katalogen
    Given att användaren navigerar till "Lägg till bok"
    When användaren fyller i författare "J.K. Rowling" och titel "Harry Potter"
    And klickar på knappen "Lägg till"
    Then ska boken "Harry Potter" visas i katalogen

  Scenario: Knappen "Lägg till" ska vara inaktiverad när fälten är tomma
    Given att användaren navigerar till "Lägg till bok"
    Then ska knappen "Lägg till" vara inaktiverad