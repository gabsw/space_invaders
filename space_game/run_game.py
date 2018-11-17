import pygame

from pygame.sprite import Group

from space_game.settings import Settings

from space_game.ship import Ship

import space_game.functions as gf

from space_game.game_stats import GameStats

from space_game.button import Button

from space_game.scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Create the Play Button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a group to store bullets in
    bullets = Group()

    # Create a group to store all the aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
