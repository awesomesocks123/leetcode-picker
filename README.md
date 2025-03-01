# Random LeetCode Problem Generator

## Overview

This is a simple Python application built using customtkinter for the GUI. It randomly selects a LeetCode problem from a predefined list (stored in a CSV file) based on the selected difficulty level (Easy, Medium, or Hard). The program also automatically opens the problem’s URL in your default web browser for quick access.

### Why I Built This

Randomized way to pick problems and also provide quick access to the picked problems directly. And also because LeetCode's website sucks and I hate going through my history to find what problems to do.

The CSV file acts as a log of problems I’ve solved, making reviewing and revisiting them easy.

### Features

- Difficulty-Based Selection: Choose between Easy, Medium, or Hard problems.

- Random Problem Generator: Instantly get a random problem from the selected difficulty level.

- Quick Access to Problems: Automatically opens the problem’s URL in your default web browser.

- Customizable Problem List: Add or remove problems from the problems.csv file to tailor the list to your needs.

### How It Works

The program reads a CSV file (problems.csv) that contains a list of LeetCode problems, their difficulty levels, and their URLs.

When you select a difficulty level (Easy, Medium, or Hard), the program randomly picks a problem from the corresponding category.

The selected problem’s name is displayed in the GUI, and its URL is automatically opened in your web browser.
