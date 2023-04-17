  gf.check_events(ship, game_settings, screen, bullets, play_button, stats, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, game_settings, screen, ship, stats, sb)  # Updating bullets.
            gf.update_aliens(game_settings, aliens, ship, stats, screen, bullets, sb)  # Update aliens.
        # Updating or loading the screen.
        gf.update_screen(game_settings, scre