# Ved.digital - Flask Web Application

## ॐ वेद • ज्ञान • प्रौद्योगिकी

A modern Flask web application inspired by Vedic wisdom and Indian culture, featuring traditional design elements with cutting-edge technology.

## Features

- **Vedic Design Elements**: Traditional Indian patterns, Om symbols (ॐ), Lotus motifs (🪷)
- **Sanskrit Integration**: Devanagari script throughout the interface
- **Saffron Color Scheme**: Traditional Indian colors (Orange, Gold, Saffron)
- **Cultural Motifs**: Mandala patterns, traditional borders, decorative elements
- **Modern Technology**: Flask, Jinja2, Tailwind CSS
- **Responsive Design**: Mobile-first approach

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access in browser:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
Ved.digital/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/               # Jinja2 templates
│   ├── base.html           # Base template with Vedic design
│   ├── index.html          # Home page
│   ├── about.html          # About page
│   ├── services.html       # Services page
│   ├── portfolio.html      # Portfolio page
│   ├── insights.html       # Insights page
│   ├── contact.html        # Contact page
│   └── partials/           # Reusable components
│       ├── navbar.html     # Navigation with Sanskrit
│       └── footer.html     # Footer with Vedic elements
└── static/                  # Static files
    ├── logo.png
    └── favicon_io/
```

## Design Elements

### Traditional Indian Colors
- **Saffron/Orange** (#FF9933): Primary color representing courage and sacrifice
- **Gold** (#FFD700): Prosperity and wisdom
- **Deep Orange** (#FF6B35): Energy and enthusiasm

### Cultural Symbols
- **ॐ (Om)**: Universal sound, spiritual symbol
- **🪷 (Lotus)**: Purity, enlightenment, and beauty
- **❋ (Decorative)**: Traditional pattern elements
- **Sanskrit Text**: Devanagari script for authenticity

### Design Features
- Mandala background patterns
- Traditional border designs (vedic-border)
- Corner decorations with symbols
- Gradient effects inspired by Indian textiles
- Glass morphism with cultural touch

## Routes

- `/` - Home page with Vedic elements
- `/about` - About page with cultural context
- `/services` - Services page
- `/portfolio` - Portfolio showcase
- `/insights` - Blog/Insights
- `/contact` - Contact form

## Technologies

- **Backend**: Flask 3.0.0
- **Frontend**: Tailwind CSS, JavaScript
- **Fonts**: 
  - Inter (Modern sans-serif)
  - Playfair Display (Elegant serif)
  - Noto Sans Devanagari (Sanskrit/Hindi)
- **Icons**: Font Awesome 6.5.1
- **Animations**: AOS (Animate On Scroll)

## Cultural Elements

### Sanskrit Translations Used
- वेद (Ved) - Knowledge
- ज्ञान (Gyan) - Wisdom
- प्रौद्योगिकी (Praudyogiki) - Technology
- सत्यमेव जयते (Satyameva Jayate) - Truth Alone Triumphs
- नवाचार (Navachar) - Innovation
- स्थायी विकास (Sthayi Vikas) - Sustainable Growth

## Customization

To modify the Vedic design elements, edit `templates/base.html`:
- Change colors in the gradient definitions
- Modify Sanskrit text in individual templates
- Adjust traditional patterns and symbols
- Update border styles and decorative elements

## License

© 2026 Ved.digital. All rights reserved.

---

**सत्यमेव जयते** • Truth Alone Triumphs
