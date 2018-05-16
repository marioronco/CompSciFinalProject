elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            bullet.bullet_movement(cursor.rect.x, cursor.rect.y, player.rect.x, player.rect.y)

    all_sprites_list.update()

    pygame.mouse.set_visible(0)

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, sprites_list, True)
        for i in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)
        for i in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # .update() will 'update' or change the screen with what
    # we've told it to everytime we run throught the loop. Without
    # this our player would not appear to move on the screen because
    # we wouldn't be telling the screen to change the coordinates of the player.
    cursor.update()
    bullet_list.update()



    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


https://stackoverflow.com/questions/33221308/bullets-arent-shooting-at-the-exact-position-of-mouse

