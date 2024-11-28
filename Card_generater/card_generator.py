import pygame
import os

# ============= CARD GENERATION CONTROLS =============
# File Paths
TEMPLATE_IMAGE = 'Flag_of_the_United_States.png'  # Base card image to modify
MAIN_TEXT_FILE = 'Main_Text.txt'      # File containing main text for cards
EFFECT1_TEXT_FILE = 'Effect_1.txt'    # File containing effect 1 text
EFFECT2_TEXT_FILE = 'Effect_2.txt'    # File containing effect 2 text

# Colors (RGB format)
MAIN_TEXT_COLOR = (0, 0, 0)  # Black
EFFECT1_TEXT_COLOR = (0, 0, 0)  # Black
EFFECT2_TEXT_COLOR = (0, 0, 0)  # Black

# Text Positions (as percentage of card height)
MAIN_TEXT_Y_POS = 0.3  # 30% from top
EFFECTS_Y_POS = 0.7   # 70% from top

# Text Area Sizes (as percentage of card dimensions)
MAIN_TEXT_WIDTH = 0.8   # 80% of card width
MAIN_TEXT_HEIGHT = 0.15 # 15% of card height
EFFECT_TEXT_WIDTH = 0.35  # 35% of card width
EFFECT_TEXT_HEIGHT = 0.12 # 12% of card height

# Font Settings
MIN_FONT_SIZE = 12
MAX_FONT_SIZE = 72
FONT_NAME = None  # None uses default system font. Change to font filename to use custom font

# Output Settings
OUTPUT_FOLDER = 'generated_cards'
OUTPUT_FORMAT = 'png'  # Options: 'png', 'jpg'
# ================================================

# Initialize Pygame
pygame.init()

def load_text_files():
    """Load content from all text files."""
    base_path = os.path.dirname(__file__)
    
    with open(os.path.join(base_path, MAIN_TEXT_FILE), 'r') as f:
        main_texts = [line.strip() for line in f if line.strip()]
    
    with open(os.path.join(base_path, EFFECT1_TEXT_FILE), 'r') as f:
        effect1_texts = [line.strip() for line in f if line.strip()]
    
    with open(os.path.join(base_path, EFFECT2_TEXT_FILE), 'r') as f:
        effect2_texts = [line.strip() for line in f if line.strip()]
    
    return main_texts, effect1_texts, effect2_texts

def get_optimal_font_size(text, max_width, max_height, start_size=MAX_FONT_SIZE):
    """Calculate the optimal font size for the given text and space."""
    font_size = start_size
    font = pygame.font.Font(FONT_NAME, font_size)
    text_surface = font.render(text, True, MAIN_TEXT_COLOR)
    
    while (text_surface.get_width() > max_width or 
           text_surface.get_height() > max_height) and font_size > MIN_FONT_SIZE:
        font_size -= 1
        font = pygame.font.Font(FONT_NAME, font_size)
        text_surface = font.render(text, True, MAIN_TEXT_COLOR)
    
    return font_size

def create_card(template_path, main_text, effect1_text, effect2_text, output_path):
    """Create a single card with the given texts."""
    # Load the template image
    template = pygame.image.load(template_path)
    card_surface = template.copy()
    
    # Calculate actual dimensions based on percentages
    card_width = card_surface.get_width()
    card_height = card_surface.get_height()
    
    main_text_area = (
        card_width * MAIN_TEXT_WIDTH,
        card_height * MAIN_TEXT_HEIGHT
    )
    effect_text_area = (
        card_width * EFFECT_TEXT_WIDTH,
        card_height * EFFECT_TEXT_HEIGHT
    )
    
    # Get optimal font sizes
    main_font_size = get_optimal_font_size(main_text, *main_text_area)
    effect1_font_size = get_optimal_font_size(effect1_text, *effect_text_area)
    effect2_font_size = get_optimal_font_size(effect2_text, *effect_text_area)
    
    # Create fonts
    main_font = pygame.font.Font(FONT_NAME, main_font_size)
    effect1_font = pygame.font.Font(FONT_NAME, effect1_font_size)
    effect2_font = pygame.font.Font(FONT_NAME, effect2_font_size)
    
    # Render texts with their respective colors
    main_text_surface = main_font.render(main_text, True, MAIN_TEXT_COLOR)
    effect1_surface = effect1_font.render(effect1_text, True, EFFECT1_TEXT_COLOR)
    effect2_surface = effect2_font.render(effect2_text, True, EFFECT2_TEXT_COLOR)
    
    # Calculate positions
    main_text_rect = main_text_surface.get_rect(
        center=(card_width // 2, card_height * MAIN_TEXT_Y_POS)
    )
    effect1_rect = effect1_surface.get_rect(
        center=(card_width // 4, card_height * EFFECTS_Y_POS)
    )
    effect2_rect = effect2_surface.get_rect(
        center=(3 * card_width // 4, card_height * EFFECTS_Y_POS)
    )
    
    # Draw texts
    card_surface.blit(main_text_surface, main_text_rect)
    card_surface.blit(effect1_surface, effect1_rect)
    card_surface.blit(effect2_surface, effect2_rect)
    
    # Save the card
    pygame.image.save(card_surface, output_path)

def generate_all_cards(template_path):
    """Generate all cards based on the text files."""
    main_texts, effect1_texts, effect2_texts = load_text_files()
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_FOLDER)
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate cards
    for i, (main_text, effect1_text, effect2_text) in enumerate(zip(main_texts, effect1_texts, effect2_texts)):
        output_path = os.path.join(output_dir, f'card_{i+1}.{OUTPUT_FORMAT}')
        create_card(template_path, main_text, effect1_text, effect2_text, output_path)
        print(f'Generated card {i+1}')

if __name__ == '__main__':
    # Path to your template image
    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_IMAGE)
    
    # Generate all cards
    generate_all_cards(template_path)
    print('All cards generated successfully!')
