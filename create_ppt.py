from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_premium_presentation():
    # Create presentation object
    prs = Presentation()

    # --- DESIGN CONSTANTS ---
    # Premium Palette
    BG_COLOR = RGBColor(35, 35, 35)       # Charcoal Dark Grey
    TITLE_COLOR = RGBColor(218, 165, 32)  # Muted Gold
    TEXT_COLOR = RGBColor(245, 245, 245)  # Off-White
    ACCENT_COLOR = RGBColor(230, 81, 0)   # Deep Orange (Terracotta/Odisha Earth)

    def apply_premium_theme(slide):
        """Applies the dark charcoal background to a slide."""
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

    def add_premium_slide(title_text, body_text_lines, layout_index=1):
        """Helper to add a slide with consistent premium formatting."""
        slide_layout = prs.slide_layouts[layout_index]
        slide = prs.slides.add_slide(slide_layout)
        apply_premium_theme(slide)

        # Format Title
        title = slide.shapes.title
        title.text = title_text
        title.text_frame.paragraphs[0].font.name = "Arial"
        title.text_frame.paragraphs[0].font.size = Pt(40)
        title.text_frame.paragraphs[0].font.bold = True
        title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR

        # Format Body Text
        if slide.placeholders[1]:
            body = slide.placeholders[1]
            tf = body.text_frame
            tf.clear()  # Clear existing placeholders
            
            for line in body_text_lines:
                p = tf.add_paragraph()
                p.text = line
                p.font.name = "Calibri"
                p.font.size = Pt(22)
                p.font.color.rgb = TEXT_COLOR
                p.space_after = Pt(14)  # Add breathing room between lines
                
                # If it's a bullet point/sub-point (starts with - or *)
                if line.startswith("  "):
                    p.level = 1

    # ==========================
    # SLIDE 1: TITLE SLIDE
    # ==========================
    slide_layout = prs.slide_layouts[0] # Title Slide Layout
    slide = prs.slides.add_slide(slide_layout)
    apply_premium_theme(slide)
    
    title = slide.shapes.title
    title.text = "LAND DEVELOPMENT IN ODISHA"
    title.text_frame.paragraphs[0].font.size = Pt(54)
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
    
    subtitle = slide.placeholders[1]
    subtitle.text = "A Journey from Ancient Settlements to Digital Bhulekh\n(3rd Century BCE – Present)"
    subtitle.text_frame.paragraphs[0].font.color.rgb = TEXT_COLOR
    subtitle.text_frame.paragraphs[0].font.size = Pt(24)

    # ==========================
    # SLIDE 2: THE HOOK
    # ==========================
    add_premium_slide(
        "Before Satellite Maps...",
        [
            "Before cadastral surveys.",
            "Before the 'Sabik–Hal' chaos.",
            "Odisha was already measuring land—with ropes, stones, and community memory.",
            "",
            "Ever wondered how Khanapuri, Bandobasta, and RORs began?",
            "Let's rewind 1,000+ years."
        ]
    )

    # ==========================
    # SLIDE 3: ANCIENT ERA
    # ==========================
    add_premium_slide(
        "3rd Century BCE: The Ancient Twist",
        [
            "Location: Kalinga",
            "Land wasn’t 'owned'… it was owed.",
            "Villagers cultivated → State took a share → Natural boundaries ruled.",
            "",
            "The OG Settlement Method:",
            "  - A bamboo stick.",
            "  - A rope.",
            "  - 4 Elders walking the field.",
            "  - 'This is yours. That is mine.'"
        ]
    )

    # ==========================
    # SLIDE 4: MEDIEVAL ERA
    # ==========================
    add_premium_slide(
        "Medieval Era: The 'Glow-Up'",
        [
            "4th – 14th Century (Ganga Dynasty)",
            "Odisha gets serious about records.",
            "",
            "Key Innovations:",
            "  - Paliyas: Stone boundary markers installed.",
            "  - Copper Plates: Land grants recorded permanently.",
            "  - New Units: 'Kulyavapa' and 'Nivartana' become standard.",
            "",
            "We invented our own cadastre long before colonial surveys."
        ]
    )

    # ==========================
    # SLIDE 5: MUGHAL & MARATHA
    # ==========================
    add_premium_slide(
        "16th-18th Century: Revenue is King",
        [
            "The Mughals brought the Math.",
            "  - Todar Mal’s Bandobasta: Land became data.",
            "  - New Units: Bigha, Biswa, and Guntha (still used today).",
            "",
            "The Marathas brought the Pressure.",
            "  - Auctions for revenue collection.",
            "  - Introduction of the 'Amil' (Revenue Officer).",
            "  - If your name wasn't in the Amil's book, you didn't exist."
        ]
    )

    # ==========================
    # SLIDE 6: BRITISH ERA
    # ==========================
    add_premium_slide(
        "1803: The Era of Chains & Maps",
        [
            "The British Surveyors Arrive.",
            "They brought the Gunter’s Chain (66 ft) and Theodolites.",
            "",
            "The Sunset Law (1803):",
            "  - If tax wasn't paid by sunset, the Zamindar lost the estate.",
            "  - Result: Ownership shifted to wealthy 'Calculators' in Calcutta.",
            "",
            "Birth of 'Sabik' (The Old Record):",
            "  - First systematic mapping. Every plot got a number."
        ]
    )

    # ==========================
    # SLIDE 7: POST-INDEPENDENCE
    # ==========================
    add_premium_slide(
        "1947 - Present: Rights & Confusion",
        [
            "1951: The OEA Act (Abolition of Zamindari).",
            "  - The Middlemen were removed.",
            "  - 'Sthitiban' status became the gold standard.",
            "",
            "The Great Conflict: Sabik vs. Hal",
            "  - Sabik: What the British recorded (Old).",
            "  - Hal: What the current settlement says (New).",
            "  - The gap between these two is where 90% of disputes live."
        ]
    )

    # ==========================
    # SLIDE 8: THE FUTURE
    # ==========================
    add_premium_slide(
        "The Future: Bhulekh & Beyond",
        [
            "From Dusty Rooms to Digital Servers.",
            "",
            "Current Tech:",
            "  - Bhulekh: Online RORs.",
            "  - Bhunaksha: Digitized Maps.",
            "",
            "Next Gen:",
            "  - Drone Surveys & Satellite Imaging.",
            "  - Moving from 'approximate boundaries' to absolute precision.",
            "  - Blockchain Land Titles."
        ]
    )

    # ==========================
    # SLIDE 9: CONCLUSION
    # ==========================
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    apply_premium_theme(slide)
    
    title = slide.shapes.title
    title.text = "DEVELOPMENT REQUIRES HISTORY"
    title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
    
    body = slide.placeholders[1]
    tf = body.text_frame
    tf.clear()
    p = tf.add_paragraph()
    p.text = "To build the future of Odisha, we must understand the layers beneath the soil.\n\nRespect the Sabik.\nVerify the Hal.\nTrust the Tech."
    p.font.size = Pt(28)
    p.font.color.rgb = TEXT_COLOR
    p.alignment = PP_ALIGN.CENTER

    # Save the presentation
    file_name = "Odisha_Land_History_Premium.pptx"
    prs.save(file_name)
    print(f"Presentation created successfully: {file_name}")

if __name__ == "__main__":
    try:
        create_premium_presentation()
    except ImportError:
        print("Error: 'python-pptx' library not found.")
        print("Please install it using: pip install python-pptx")