# Teorifrågor

## 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

- **Enhetstest:** Testar en enskild metod eller klass för att kontrollera att den fungerar som förväntat.
- **Integrationstest:** Testar att flera delar fungerar tillsammans, till exempel `BookStore` och `FavoriteBooks`.
- **Regressionstest:** Kontrollerar att tidigare fungerande funktionalitet fortfarande fungerar efter ändringar i koden.
- **Prestandatest:** Undersöker hur snabbt och stabilt systemet fungerar vid olika belastningar.

## 2. Beskriv hur det går till när man arbetar med TDD.

TDD står för Test-Driven Development. Man börjar med att skriva ett test för den önskade funktionaliteten. Först kör man testet och kontrollerar att det misslyckas (Red). Sedan skriver man den minsta mängd kod som behövs för att testet ska passera (Green). Till sist förbättrar man koden utan att ändra funktionaliteten (Refactor).

## 3. Beskriv hur BDD skiljer sig från TDD.

TDD fokuserar på att utveckla och testa kod genom små tester, ofta på metodnivå. BDD fokuserar på systemets beteende ur användarens perspektiv. Krav beskrivs ofta med exempel i formatet Given, When, Then. BDD gör det lättare att förstå och kommunicera hur systemet ska fungera.

## 4. Vilka sorters tester skulle du vilja använda för en webbsida som Läslistan? Motivera ditt val.

Jag skulle använda flera typer av tester:

- **Enhetstester:** För att testa backendens metoder, till exempel att lägga till böcker och ändra favoritstatus.
- **Integrationstester:** För att kontrollera att backendens olika klasser fungerar tillsammans.
- **API-tester:** För att kontrollera att frontend och backend kommunicerar korrekt via API:er.
- **End-to-end-tester:** Med exempelvis Playwright för att testa hela användarflöden i webbläsaren, till exempel att lägga till en bok och markera den som favorit.
- **Regressionstester:** För att kontrollera att befintlig funktionalitet fortfarande fungerar efter kodändringar.
- **Prestandatester:** För att kontrollera att sidan fungerar snabbt och stabilt även när många användare använder den samtidigt.

Jag skulle prioritera enhetstester och integrationstester för backend samt end-to-end-tester för de viktigaste användarflödena. På så sätt kan fel upptäckas på olika nivåer och systemets grundläggande funktionalitet kontrolleras.