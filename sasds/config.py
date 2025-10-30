"""Configuration settings for the SASDS project"""
# Configuration settings
import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///sasds.db')
