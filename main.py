import pygame

# Käivita pygame
pygame.init()

# Seadista ekraani suurus
screen_width = 640 # Määrame ekraani laiuse
screen_height = 480 # määrame ekraani pikkuse 
screen = pygame.display.set_mode((screen_width, screen_height)) # anname screenile väärtuse
pygame.display.set_caption('Karl Paju IS22') # loome ekraanile nime 

# Laadi pildid
platform_image = pygame.image.load('pad.png').convert_alpha() # laeme platvormi pildi
ball_image = pygame.image.load('ball-1.webp').convert_alpha() # laeme palli pildi

# Määrame platvormi ja palli algasukohad
platform_x = screen_width / 2 - platform_image.get_width() / 2 # määrame platvormi x asukoha 
platform_y = screen_height - platform_image.get_height() - 50 # määrame platvormi y asukoha
ball_x = screen_width / 2 - ball_image.get_width() / 2 # määrame palli x asukoha
ball_y = platform_y - ball_image.get_height() # määrame palli y asukoha

# Määrame palli algne kiirus
ball_speed_x = 5 # määrame palli x kiiruse
ball_speed_y = -5 # määrame palli y kiiruse

# Määra platvormi kiirus
platform_speed = 10 # määrame platvormi kiiruse

# Määra algne skoor
score = 0 # määrame algse skoori

# Määra fondi suurus skoori kuvamiseks
font = pygame.font.SysFont(None, 36) # Määrame fondi


# Defineeri mäng läbi funktsioon
def game_over():
    # Kuva mäng läbi teade
    game_over_text = font.render("Mäng läbi!", True, (255, 0, 0)) # Loome game over teksti, mis ilmub ekraanile
    screen.blit(game_over_text, (
        screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2)) # loome selle ekraani keskele

    # Kuva lõppskoor
    final_score_text = font.render(f"Lõpp tulemus: {score}", True, (0, 0, 0)) # kuvame ekraanile lõpptulemuse
    screen.blit(final_score_text, (
        screen_width / 2 - final_score_text.get_width() / 2, screen_height / 2 + game_over_text.get_height() / 2)) # määrame asukoha lõpptulemuseks

    # uuenda ekraani
    pygame.display.update() # uuendame ekraani

    # Oota mõned sekundid enne lõpetamist
    pygame.time.wait(3000) # ootame 3 sek enne lõpetamist
    pygame.quit() # sulgemine 
    exit() # mäng läheb kinni


# Alusta mängu loop-i
while True:
    # Tee sündmustega tegelemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Liiguta platvormi
    keys = pygame.key.get_pressed() # anname keys muutujale väärtuse
    if keys[pygame.K_LEFT] and platform_x > 0: # kui vajutame  vasak klahvi liigub platvorm x teljel vasakule
        platform_x -= platform_speed # kiirus muutub negatiivseks
    if keys[pygame.K_RIGHT] and platform_x + platform_image.get_width() < screen_width: # kui vajutame paremat klahvi liigub platvorm x teljel paremale
        platform_x += platform_speed # kiirus muutub positiivseks

    # Liiguta palli
    ball_x += ball_speed_x # anname muutujale väärtuse
    ball_y += ball_speed_y # anname muutujuale väärtuse

    # Põruta pall tagasi seintest
    if ball_x < 0 or ball_x + ball_image.get_width() > screen_width: # kui pall on väiksem x teljega ning laiusega kui ekraani laius
        ball_speed_x = -ball_speed_x # siis muudame palli kiiruse x teljel negatiivseks
    if ball_y < 0: # kui pall on y teljel väiksem kui null
        ball_speed_y = -ball_speed_y # siis muudame palli kiiruse y teljel negatiivseks
    elif ball_y + ball_image.get_height() > screen_height: # aga kui pall on suurema pikkusega kui ekraani pikkus
        # Mäng läbi
        game_over() # siis on mäng läbi

    # Kontrollime kas pall läheb platformi vastu
    if ball_y + ball_image.get_height() > platform_y and \ # kui pall on väiksem y teljel kui platvorm
            ball_x + ball_image.get_width() > platform_x and \ # kui palli laius on väiksem x teljel kui platvormil
            ball_x < platform_x + platform_image.get_width(): # kui pall on väiksem x teljel kui platvorm siis
        ball_speed_y = -ball_speed_y # kui platvormi vastu läheb pall siis ta kiirus vastandub negatiivseks 
        score += 1 # kui pall läheb platvormi vastu saab lisa ühe punkti

    # Clear the screen
    screen.fill((255, 255, 255)) # tühjendame ekraani

    # Draw the images
    screen.blit(platform_image, (platform_x, platform_y)) # joonistame ekraanile platvormi
    screen.blit(ball_image, (ball_x, ball_y)) # joonistame ekraanile palli

    # Joonistame ekraanile skoori
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0)) # loome muutujale väärtuse
    screen.blit(score_text, (10, 10)) # loome skoori asukoha

    # Uuendab ekraani
    pygame.display.update() # uuendame ekraani

    # Sätime fpsi
    pygame.time.Clock().tick(120) # Sätime fpsi 
