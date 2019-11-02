        # check if a bullet hit an asteroid
        asteroid_hit = pygame.sprite.groupcollide(asteroids, bullets, True, pygame.sprite.collide_circle)
        # when asteroids are destroyed, spawn new asteroids
        for hit in asteroid_hit:
            score += 50 - hit.radius # different scores for different size asteroids
            large_expl.play()
            large_expl.set_volume(0.1)
            expl = Explosion(hit.rect.center, 'large', explosion_anim)
            all_active_sprites.add(expl)
            if random.random() > 0.92:
                powerup = PowerUp(hit.rect.center, powerup_images)
                all_active_sprites.add(powerup)
                powerups.add(powerup)
            new_asteroid = Asteroid(asteroid_images, all_active_sprites, asteroids)
            all_active_sprites.add(new_asteroid)
            asteroids.add(new_asteroid)
        # check if a bullet hit an asteroid
        asteroid_hit = pygame.sprite.groupcollide(asteroids, bullets, True, pygame.sprite.collide_circle)
        # when asteroids are destroyed, spawn new asteroids
        for hit in asteroid_hit:
            score += 50 - hit.radius # different scores for different size asteroids
            large_expl.play()
            large_expl.set_volume(0.1)
            expl = Explosion(hit.rect.center, 'large', explosion_anim)
            all_active_sprites.add(expl)
            if random.random() > 0.92:
                powerup = PowerUp(hit.rect.center, powerup_images)
                all_active_sprites.add(powerup)
                powerups.add(powerup)
            new_asteroid = Asteroid(asteroid_images, all_active_sprites, asteroids)
            all_active_sprites.add(new_asteroid)
            asteroids.add(new_asteroid)