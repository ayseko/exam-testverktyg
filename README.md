# Läslistan – Testverktyg

## Beskrivning

Detta projekt innehåller tester för bokapplikationen Läslistan. Projektet använder pytest för unit- och integrationstester samt Behave och Playwright för BDD-tester av användargränssnittet.

Webbapplikationen som testas finns på:

https://tap-vt26-testautomatisering.github.io/exam/

Detta projekt innehåller testkod för webbapplikationen. Applikationen körs separat, medan testerna körs lokalt eller automatiskt via GitHub Actions.

## Tekniker

- Python
- pytest
- Behave
- Playwright
- Gherkin

## Projektstruktur

- `src/` – applikationens Python-klasser
- `tests/unit/` – unit-tester
- `tests/integration/` – integrationstester
- `tests/features/` – BDD-scenarier
- `tests/features/steps/` – implementerade stegdefinitioner

## Installation

Installera beroendena med:

```bash
pip install -r requirements.txt
```

Installera Playwrights Chromium-webbläsare vid behov:

```bash
python -m playwright install chromium
```

## Köra tester

Kör unit- och integrationstester:

```bash
python -m pytest tests/unit tests/integration -v
```

Kör alla BDD-tester:

```bash
python -m behave tests/features
```

Kör alla pytest-tester:

```bash
python -m pytest
```

## Testområden

BDD-testerna omfattar katalogen, att lägga till en bok och att visa samt ta bort favoritböcker. Unit- och integrationstesterna kontrollerar funktionaliteten i `BookStore` och `FavoriteBooks`.