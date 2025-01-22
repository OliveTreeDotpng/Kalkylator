import os

# Skapar en konfigurationsklass för att hantera inställningar i applikationen.
class Config:
    # Hemlig nyckel som används för säkerhet, t.ex. för att skydda sessionsdata och för kryptering.
    SECRET_KEY = os.getenv("SECRET_KEY", "a2c4d3e7fba893d2c4a12e9d0b6d3f47c9e0a789123f3a56a1b7c2d4e8f9a0b1")

    # Databasens URI (adress) som anger var databasen finns.
    # Hämtas från miljövariabeln "DATABASE_URL"
    # Standardvärdet är en SQLite-databas som skapas i filen "calculator.db".
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///calculator.db")


    # Förbättrar prestanda genom att inaktivera spårning av ändringar
    SQLALCHEMY_TRACK_MODIFICATIONS = False
