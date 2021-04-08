import pygame, pygame.image, pygame.display, pygame.event, pygame.mixer, pygame.mouse, pygame.transform, pyautogui, random, sys, time, os
class Application():
    def __init__(self):
        global volume
        global score
        global match_num
        global got_the_game
        global beat_the_game
        global thousand_miles_travelled
        self.map = ['', '', '', '', '', '', '', '', '']
        self.screen = pygame.display.set_mode((1920, 1080))
        file = open(os.path.join('tic_tac_toe_data', 'settings_and_data.txt'), 'r+')
        data_and_settings = file.read().split('\n')
        score = int(data_and_settings[1])
        volume = float(data_and_settings[0]) / 100
        match_num, got_the_game, beat_the_game, thousand_miles_travelled = int(data_and_settings[2]), data_and_settings[3], data_and_settings[4], data_and_settings[5]
    def run_main_menu(self):
        global volume
        global score
        global match_num
        global got_the_game
        global beat_the_game
        global thousand_miles_travelled
        global action
        action = ''
        self.map = ['', '', '', '', '', '', '', '', '']
        pygame.init()
        pygame.mixer.init()
        start = pygame.image.load(os.path.join('tic_tac_toe_data', 'start_tic_tac_toe.png'))
        settings = pygame.image.load(os.path.join('tic_tac_toe_data', 'settings_tic_tac_toe.png'))
        stats = pygame.image.load(os.path.join('tic_tac_toe_data', 'stats_tic_tac_toe.png'))
        tutorial = pygame.image.load(os.path.join('tic_tac_toe_data', 'tutorial_tic_tac_toe.png'))
        background_random = [pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_1.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_2.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_3.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_4.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_5.png'))]
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.queue(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.play(-1)
        while True:
            if score >= 100000 and beat_the_game != '1 1':
                beat_the_game = '1 0'
            if match_num >= 1000 and thousand_miles_travelled != '1 1':
                thousand_miles_travelled = '1 0'
            if got_the_game[0] != '1':
                got_the_game = '1 0'
            if got_the_game[0] == '1' and got_the_game[2] == '0':
                pyautogui.alert(text = 'Hello! Thank you for installing this game! Have fun!', title = 'Welcome', button = 'OK')
                got_the_game = '1 1'
            if beat_the_game[0] == '1' and beat_the_game[2] == '0':
                pyautogui.alert(text = 'Congratulations! You\'ve gained over 100,000 points, which means you have beaten the game!', title = 'Congratulations', button = 'OK')
                beat_the_game = '1 1'
            if thousand_miles_travelled[0] == '1' and thousand_miles_travelled[2] == '0':
                pyautogui.alert(text = 'YOU\'RE INSANE! YOU\'VE BEATEN THE COMPUTER IN 1000 MATCHES!', title = '1000 Matches', button = 'OK')
                thousand_miles_travelled = '1 1'
            self.screen.fill((0, 0, 0))
            self.screen.blit(background_random[random.randint(0, 4)], (0, 0))
            self.screen.blit(start, (50, 50))
            self.screen.blit(settings, (1570, 50))
            self.screen.blit(stats, (830, 200))
            self.screen.blit(tutorial, (910, 600))
            start_rect = start.get_rect()
            settings_rect = settings.get_rect()
            stats_rect = stats.get_rect()
            tutorial_rect = tutorial.get_rect()
            start_rect.width, start_rect.height, start_rect.centerx, start_rect.centery = 300, 100, 200, 100
            settings_rect.width, settings_rect.height, settings_rect.centerx, settings_rect.centery = 300, 100, 1720, 100
            stats_rect.width, stats_rect.height, stats_rect.centerx, stats_rect.centery = 260, 100, 960, 250
            tutorial_rect.width, tutorial_rect.height, tutorial_rect.centerx, tutorial_rect.centery = 100, 200, 1010, 700
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    for i in range(255):
                        self.screen.fill((i, i, i))
                        pygame.display.flip()
                    volume = int(volume * 100)
                    file = open(os.path.join('tic_tac_toe_data', 'settings_and_data.txt'), 'r+')
                    file.write(f'{volume}\n{score}\n{match_num}\n{got_the_game}\n{beat_the_game}\n{thousand_miles_travelled}')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if start_rect.collidepoint(x, y):
                        action = 'play'
                        for i in range(255):
                            self.screen.fill((0, 0, i))
                            pygame.display.flip()
                        return
                    elif settings_rect.collidepoint(x, y):
                        action = 'settings'
                        return
                    elif stats_rect.collidepoint(x, y):
                        stat_list = ['You currently have a score of ']
                        stat_list_2 = ['Your achievements are:']
                        if score >= 100000:
                            stat_list.append(f'{score}. Wow, that\'s pretty insane!')
                        elif score >= 1000:
                            stat_list.append(f'{score}. Not bad!')
                        else:
                            stat_list.append(f'{score}. Not the best, but you\'ll improve.')
                        if got_the_game[0] == '1':
                            stat_list_2.append('Got The Game')
                        if beat_the_game[0] == '1':
                            stat_list_2.append('Beat The Game')
                        if thousand_miles_travelled[0] == '1':
                            stat_list_2.append('One Thousand Miles Travelled')
                        stat_list = ''.join(stat_list)
                        stat_list_2 = '\n'.join(stat_list_2)
                        pyautogui.alert(text = f'{stat_list}\n\nYou\'ve played and won {match_num} matches.\n\n{stat_list_2}', title = 'Stats', button = 'OK')
                    elif tutorial_rect.collidepoint(x, y):
                        action = 'tutorial'
                        for i in range(255):
                            self.screen.fill((0, 0, i))
                            pygame.display.flip()
                        return
            pygame.display.flip()
    def run_settings(self):
        global volume
        global score
        global match_num
        global got_the_game
        global beat_the_game
        global thousand_miles_travelled
        pygame.init()
        pygame.mixer.init()
        background_random = [pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_1.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_2.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_3.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_4.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_5.png'))]
        slider = pygame.transform.scale(pygame.image.load(os.path.join('tic_tac_toe_data', 'slider_tic_tac_toe.png')), (200, 500))
        slider_line = pygame.image.load(os.path.join('tic_tac_toe_data', 'slider_line.png'))
        volume_text = pygame.image.load(os.path.join('tic_tac_toe_data', 'vol_recommendation.png'))
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.queue(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.play(-1)
        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(background_random[random.randint(0, 4)], (0, 0))
            self.screen.blit(slider_line, (0, 0))
            self.screen.blit(volume_text, (550, 800))
            if volume == 0.2:
                self.screen.blit(slider, (0, 250))
            elif volume == 0.4:
                self.screen.blit(slider, (384, 250))
            elif volume == 0.6:
                self.screen.blit(slider, (768, 250))
            elif volume == 0.8:
                self.screen.blit(slider, (1152, 250))
            elif volume == 1.0:
                self.screen.blit(slider, (1536, 250))
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
                    volume = 0.0
                    pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    volume = 0.2
                    pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    volume = 0.4
                    pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    volume = 0.6
                    pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    volume = 0.8
                    pygame.mixer.music.set_volume(volume)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    volume = 1.0
                    pygame.mixer.music.set_volume(volume)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            pygame.display.flip()
    def run_tutorial(self):
        global volume
        global score
        global match_num
        global got_the_game
        global beat_the_game
        global thousand_miles_travelled
        pygame.init()
        pygame.mixer.init()
        tutorial_background = pygame.image.load(os.path.join('tic_tac_toe_data', 'tutorial_background.png'))
        tutorial_1 = pygame.image.load(os.path.join('tic_tac_toe_data', 'tutorial_1.png'))
        tutorial_2 = pygame.image.load(os.path.join('tic_tac_toe_data', 'tutorial_2.png'))
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.queue(os.path.join('tic_tac_toe_data', 'menu_theme.ogg'))
        pygame.mixer.music.play(-1)
        while True:
            bg_move_x = 0
            self.screen.fill((15, 136, 161))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    for i in range(255):
                        self.screen.fill((0, 0, 255 - i))
                        pygame.display.flip()
            while bg_move_x != -300:
                bg_move_x -= 10
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        for i in range(255):
                            self.screen.fill((0, 0, 255 - i))
                            pygame.display.flip()
                        return
                self.screen.blit(tutorial_background, (bg_move_x, 0))
                self.screen.blit(tutorial_1, (350, 200))
                self.screen.blit(tutorial_2, (350, 500))
                pygame.display.flip()
            while bg_move_x != 100:
                bg_move_x += 10
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        for i in range(255):
                            self.screen.fill((0, 0, 255 - i))
                            pygame.display.flip()
                        return
                self.screen.blit(tutorial_background, (bg_move_x, 0))
                self.screen.blit(tutorial_1, (350, 200))
                self.screen.blit(tutorial_2, (350, 500))
                pygame.display.flip()
    def run_game(self):
        global volume
        global score
        global match_num
        global got_the_game
        global beat_the_game
        global thousand_miles_travelled
        def run_logic(input, map):
            map[input] = 'x'
            if self.map[0] == '' or self.map[1] == '' or self.map[2] == '' or self.map[3] == '' or self.map[4] == '' or self.map[5] == '' or self.map[6] == '' or self.map[7] == '' or self.map[8] == '':
                num = random.randint(0, 8)
                while True:
                    if map[num] == 'x' or map[num] == 'o':
                        num = random.randint(0, 8)
                    else:
                        map[num] = 'o'
                        break
                return map
            else:
                return map
        pygame.init()
        pygame.mixer.init()
        background_random = [pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_1.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_2.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_3.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_4.png')), pygame.image.load(os.path.join('tic_tac_toe_data', 'electricity_frame_5.png'))]
        bg_map = pygame.image.load(os.path.join('tic_tac_toe_data', 'tic_tac_toe_map.png'))
        x = pygame.image.load(os.path.join('tic_tac_toe_data', 'tic_tac_toe_x.png'))
        o = pygame.image.load(os.path.join('tic_tac_toe_data', 'tic_tac_toe_o.png'))
        empty_1 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_2 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_3 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_4 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_5 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_6 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_7 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_8 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_9 = pygame.image.load(os.path.join('tic_tac_toe_data', 'empty.png'))
        empty_1_rect, empty_2_rect, empty_3_rect, empty_4_rect, empty_5_rect, empty_6_rect, empty_7_rect, empty_8_rect, empty_9_rect = empty_1.get_rect(), empty_2.get_rect(), empty_3.get_rect(), empty_4.get_rect(), empty_5.get_rect(), empty_6.get_rect(), empty_7.get_rect(), empty_8.get_rect(), empty_9.get_rect()
        empty_1_rect.width, empty_1_rect.height, empty_1_rect.centerx, empty_1_rect.centery = 300, 300, 330, 160
        empty_2_rect.width, empty_2_rect.height, empty_2_rect.centerx, empty_2_rect.centery = 300, 300, 1020, 160
        empty_3_rect.width, empty_3_rect.height, empty_3_rect.centerx, empty_3_rect.centery = 300, 300, 1670, 160
        empty_4_rect.width, empty_4_rect.height, empty_4_rect.centerx, empty_4_rect.centery = 300, 300, 330, 550
        empty_5_rect.width, empty_5_rect.height, empty_5_rect.centerx, empty_5_rect.centery = 300, 300, 1020, 550
        empty_6_rect.width, empty_6_rect.height, empty_6_rect.centerx, empty_6_rect.centery = 300, 300, 1670, 550
        empty_7_rect.width, empty_7_rect.height, empty_7_rect.centerx, empty_7_rect.centery = 300, 300, 330, 910
        empty_8_rect.width, empty_8_rect.height, empty_8_rect.centerx, empty_8_rect.centery = 300, 300, 1020, 910
        empty_9_rect.width, empty_9_rect.height, empty_9_rect.centerx, empty_9_rect.centery = 300, 300, 1670, 910
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(os.path.join('tic_tac_toe_data', 'game_time_ultimate.ogg'))
        pygame.mixer.music.queue(os.path.join('tic_tac_toe_data', 'game_time_ultimate.ogg'))
        pygame.mixer.music.play(-1)
        start_time = time.time()
        def blit_tacs():
            if self.map[0] == 'x':
                self.screen.blit(x, (180, 10))
            elif self.map[0] == 'o':
                self.screen.blit(o, (180, 10))
            if self.map[1] == 'x':
                self.screen.blit(x, (870, 10))
            elif self.map[1] == 'o':
                self.screen.blit(o, (870, 10))
            if self.map[2] == 'x':
                self.screen.blit(x, (1520, 10))
            elif self.map[2] == 'o':
                self.screen.blit(o, (1520, 10))
            if self.map[3] == 'x':
                self.screen.blit(x, (180, 400))
            elif self.map[3] == 'o':
                self.screen.blit(o, (180, 400))
            if self.map[4] == 'x':
                self.screen.blit(x, (870, 400))
            elif self.map[4] == 'o':
                self.screen.blit(o, (870, 400))
            if self.map[5] == 'x':
                self.screen.blit(x, (1520, 400))
            elif self.map[5] == 'o':
                self.screen.blit(o, (1520, 400))
            if self.map[6] == 'x':
                self.screen.blit(x, (180, 760))
            elif self.map[6] == 'o':
                self.screen.blit(o, (180, 760))
            if self.map[7] == 'x':
                self.screen.blit(x, (870, 760))
            elif self.map[7] == 'o':
                self.screen.blit(o, (870, 760))
            if self.map[8] == 'x':
                self.screen.blit(x, (1520, 760))
            elif self.map[8] == 'o':
                self.screen.blit(o, (1520, 760))
            self.screen.blit(empty_1, (180, 10))
            self.screen.blit(empty_2, (870, 10))
            self.screen.blit(empty_3, (1520, 10))
            self.screen.blit(empty_4, (180, 400))
            self.screen.blit(empty_5, (870, 400))
            self.screen.blit(empty_6, (1520, 400))
            self.screen.blit(empty_7, (180, 760))
            self.screen.blit(empty_8, (870, 760))
            self.screen.blit(empty_9, (1520, 760))
        while True:
            self.screen.fill((0, 0, 255))
            self.screen.blit(background_random[random.randint(0, 4)], (0, 0))
            self.screen.blit(bg_map, (0, 0))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    for i in range(255):
                        self.screen.fill((0, 0, 255 - i))
                        pygame.display.flip()
                    return
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_1 and self.map[0] != 'o' and self.map[0] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[0] != 'o' and self.map[0] != 'x' and empty_1_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(0, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_1 and (self.map[0] == 'o' or self.map[0] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[0] == 'o' or self.map[0] == 'x') and empty_1_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The first spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_2 and self.map[1] != 'o' and self.map[1] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[1] != 'o' and self.map[1] != 'x' and empty_2_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(1, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_2 and (self.map[1] == 'o' or self.map[1] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[1] == 'o' or self.map[1] == 'x') and empty_2_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The second spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_3 and self.map[2] != 'o' and self.map[2] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[2] != 'o' and self.map[2] != 'x' and empty_3_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(2, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_3 and (self.map[2] == 'o' or self.map[2] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[2] == 'o' or self.map[2] == 'x') and empty_3_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The third spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4 and self.map[3] != 'o' and self.map[3] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[3] != 'o' and self.map[3] != 'x' and empty_4_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(3, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_4 and (self.map[3] == 'o' or self.map[3] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[3] == 'o' or self.map[3] == 'x') and empty_4_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The fourth spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_5 and self.map[4] != 'o' and self.map[4] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[4] != 'o' and self.map[4] != 'x' and empty_5_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(4, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_5 and (self.map[4] == 'o' or self.map[4] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[4] == 'o' or self.map[4] == 'x') and empty_5_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The fifth spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_6 and self.map[5] != 'o' and self.map[5] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[5] != 'o' and self.map[5] != 'x' and empty_6_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(5, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_6 and (self.map[5] == 'o' or self.map[5] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[5] == 'o' or self.map[5] == 'x') and empty_6_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The sixth spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_7 and self.map[6] != 'o' and self.map[6] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[6] != 'o' or self.map[6] != 'x') and empty_7_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(6, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_7 and (self.map[6] == 'o' or self.map[6] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.map[6] == 'o' and self.map[6] == 'x' and empty_7_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The seventh spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_8 and self.map[7] != 'o' and self.map[7] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[7] != 'o' or self.map[7] != 'x') and empty_8_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(7, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_8 and (self.map[7] == 'o' or self.map[7] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[7] == 'o' or self.map[7] == 'x') and empty_8_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The eighth spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_9 and self.map[8] != 'o' and self.map[8] != 'x') or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[8] != 'o' or self.map[8] != 'x') and empty_9_rect.collidepoint(mouse_x, mouse_y)):
                    self.map = run_logic(8, self.map)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_9 and (self.map[8] == 'o' or self.map[8] == 'x')) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (self.map[8] == 'o' or self.map[8] == 'x') and empty_9_rect.collidepoint(mouse_x, mouse_y)):
                    pyautogui.alert(text = 'The ninth spot has already been filled! Please choose another spot to place your X.', title = 'Spot Already Filled', button = 'OK')
            if ((self.map[0] == 'x' and self.map[1] == 'x' and self.map[2] == 'x') or (self.map[0] == 'x' and self.map[4] == 'x' and self.map[8] == 'x') or (self.map[2] == 'x' and self.map[4] == 'x' and self.map[6] == 'x') or (self.map[3] == 'x' and self.map[4] == 'x' and self.map[5] == 'x') or (self.map[6] == 'x' and self.map[7] == 'x' and self.map[8] == 'x') or (self.map[0] == 'x' and self.map[3] == 'x' and self.map[6] == 'x') or (self.map[1] == 'x' and self.map[4] == 'x' and self.map[7] == 'x') or (self.map[2] == 'x' and self.map[5] == 'x' and self.map[8] == 'x')) and ((self.map[0] == 'o' and self.map[1] == 'o' and self.map[2] == 'o') or (self.map[0] == 'o' and self.map[4] == 'o' and self.map[8] == 'o') or (self.map[2] == 'o' and self.map[4] == 'o' and self.map[6] == 'o') or (self.map[3] == 'o' and self.map[4] == 'o' and self.map[5] == 'o') or (self.map[6] == 'o' and self.map[7] == 'o' and self.map[8] == 'o') or (self.map[0] == 'o' and self.map[3] == 'o' and self.map[6] == 'o') or (self.map[1] == 'o' and self.map[4] == 'o' and self.map[7] == 'o') or (self.map[2] == 'o' and self.map[5] == 'o' and self.map[8] == 'o')):
                blit_tacs()
                pygame.display.flip()
                pyautogui.alert(text = 'It\'s a tie! Press OK to close this text box and exit to the main menu.', title = 'Tie', button = 'OK')
                for i in range(255):
                    self.screen.fill((0, 0, 255 - i))
                    pygame.display.flip()
                return
            elif (self.map[0] == 'x' and self.map[1] == 'x' and self.map[2] == 'x') or (self.map[0] == 'x' and self.map[4] == 'x' and self.map[8] == 'x') or (self.map[2] == 'x' and self.map[4] == 'x' and self.map[6] == 'x') or (self.map[3] == 'x' and self.map[4] == 'x' and self.map[5] == 'x') or (self.map[6] == 'x' and self.map[7] == 'x' and self.map[8] == 'x') or (self.map[0] == 'x' and self.map[3] == 'x' and self.map[6] == 'x') or (self.map[1] == 'x' and self.map[4] == 'x' and self.map[7] == 'x') or (self.map[2] == 'x' and self.map[5] == 'x' and self.map[8] == 'x'):
                end_time = time.time()
                result_score = round(start_time - end_time) * 10 + random.randint(500, 1000)
                if result_score < 0:
                    result_score = 0
                score += result_score
                match_num += 1
                blit_tacs()
                pygame.display.flip()
                pyautogui.alert(text = f'YOU WIN! Press OK to exit to the menu. Your score was {result_score}.', title = 'Victory', button = 'OK')
                for i in range(255):
                    self.screen.fill((0, 0, 255 - i))
                    pygame.display.flip()
                return
            elif (self.map[0] == 'o' and self.map[1] == 'o' and self.map[2] == 'o') or (self.map[0] == 'o' and self.map[4] == 'o' and self.map[8] == 'o') or (self.map[2] == 'o' and self.map[4] == 'o' and self.map[6] == 'o') or (self.map[3] == 'o' and self.map[4] == 'o' and self.map[5] == 'o') or (self.map[6] == 'o' and self.map[7] == 'o' and self.map[8] == 'o') or (self.map[0] == 'o' and self.map[3] == 'o' and self.map[6] == 'o') or (self.map[1] == 'o' and self.map[4] == 'o' and self.map[7] == 'o') or (self.map[2] == 'o' and self.map[5] == 'o' and self.map[8] == 'o'):
                blit_tacs()
                pygame.display.flip()
                pyautogui.alert(text = 'YOU LOST! Press OK to exit to the menu.', title = 'Loss', button = 'OK')
                for i in range(255):
                    self.screen.fill((0, 0, 255 - i))
                    pygame.display.flip()
                return
            if self.map[0] != '' and self.map[1] != '' and self.map[2] != '' and self.map[3] != '' and self.map[4] != '' and self.map[5] != '' and self.map[6] != '' and self.map[7] != '' and self.map[8] != '':
                blit_tacs()
                pygame.display.flip()
                pyautogui.alert(text = 'It\'s a tie! Press OK to close this text box and exit to the main menu.', title = 'Tie', button = 'OK')
                for i in range(255):
                    self.screen.fill((0, 0, 255 - i))
                    pygame.display.flip()
                return
            blit_tacs()
            pygame.display.flip()
application = Application()
while True:
    application.run_main_menu()
    if action == 'play':
        application.run_game()
    elif action == 'settings':
        application.run_settings()
    elif action == 'tutorial':
        application.run_tutorial()
