import random
from collections import deque

class Card:
    def __init__(self, name, meaning, orientation):
        self.name = name
        self.meaning = meaning
        self.orientation = orientation


    ORIENTATION_MEANINGS = {
        "Facing up": "Positive, or what is asked for is coming to pass.",
        "Upside down": "Negative, or what is asked for is not coming to pass."
    }


category = input("What are you asking the tarot cards: ")

cards = deque([
    Card("The Fool", "New beginnings, spontaneity, trust in the universe", None),
    Card("The Magician", "Power, concentration, resourcefulness", None),
    Card("The High Priestess", "Intuition, mystery, inner knowledge", None),
    Card("The Empress", "Abundance, fertility, femininity", None),
    Card("The Emperor", "Authority, structure, protection", None),
    Card("The Hierophant", "Tradition, beliefs, education", None),
    Card("The Lovers", "Love, harmony, relationships", None),
    Card("The Chariot", "Determination, courage, victory", None),
    Card("Strength", "Courage, strength, determination", None),
    Card("The Hermit", "Introspection, inner guidance, prudence", None),
    Card("Wheel of Fortune", "Good luck, karma, destiny", None),
    Card("Justice", "Justice, fairness, truth", None),
    Card("The Hanged Man", "Sacrifice, change, reversal", None),
    Card("Death", "Transformation, endings, rebirth", None),
    Card("Temperance", "Moderation, balance, harmony", None),
    Card("The Devil", "Temptation, materialism, addiction", None),
    Card("The Tower", "Catastrophe, upheaval, unexpected change", None),
    Card("The Star", "Hope, optimism, serenity", None),
    Card("The Moon", "Illusion, fear, intuition", None),
    Card("The Sun", "Enlightenment, happiness, vitality", None),
    Card("Judgement", "Inner calling, absolution, awakening", None),
    Card("The World", "Completion, success, journey's end", None),
    Card("Ace of Wands", "Initiative, creativity, energy", None),
    Card("Two of Wands", "Ambition, planning, courage", None),
    Card("Three of Wands", "Exploration, expansion, growth", None),
    Card("Four of Wands", "Celebration, stability, rest", None),
    Card("Five of Wands", "Competition, conflict, ambition", None),
    Card("Six of Wands", "Victory, success, pride", None),
    Card("Seven of Wands", "Courage, perseverance, defense", None),
    Card("Eight of Wands", "Speed, action, progress", None),
    Card("Nine of Wands", "Resilience, strength, tenacity", None),
    Card("Ten of Wands", "Overextension, burden, oppression", None),
    Card("Page of Wands", "Innovation, exploration, enthusiasm", None),
    Card("Knight of Wands", "Passion, adventure, impulsiveness", None),
    Card("Queen of Wands", "Charisma, leadership, courage", None),
    Card("King of Wands", "Authority, confidence, power", None),
    Card("Ace of Cups", "Emotions, love, compassion", None),
    Card("Two of Cups", "Connection, balance, harmony", None),
    Card("Three of Cups", "Celebration, friendship, joy", None),
    Card("Four of Cups", "Contemplation, introspection, apathy", None),
    Card("Five of Cups", "Loss, regret, disappointment", None),
    Card("Six of Cups", "Nostalgia, childhood, innocence", None),
    Card("Seven of Cups", "Imagination, wishful thinking, choices", None),
    Card("Eight of Cups", "Moving on, inner journey, journey", None),
    Card("Nine of Cups", "Happiness, contentment, satisfaction", None),
    Card("Ten of Cups", "Family, community, harmony", None),
    Card("Page of Cups", "Inquisitiveness, creativity, imagination", None),
    Card("Knight of Cups", "Romance, creativity, emotion", None),
    Card("Queen of Cups", "Intuition, empathy, compassion", None),
    Card("King of Cups", "Wisdom, diplomacy, calmness", None),
    Card("Ace of Swords", "Truth, justice, clarity", None),
    Card("Two of Swords", "Stalemate, inner conflict, indecision", None),
    Card("Three of Swords", "Heartache, sorrow, pain", None),
    Card("Four of Swords", "Rest, recuperation, contemplation", None),
    Card("Five of Swords", "Defeat, humiliation, loss", None),
    Card("Six of Swords", "Transition, moving on, healing", None),
    Card("Seven of Swords", "Deception, thievery, cunning", None),
    Card("Eight of Swords", "Restriction, imprisonment, confusion", None),
    Card("Nine of Swords", "Anxiety, fear, worry", None),
    Card("Ten of Swords", "Failure, defeat, end of a situation", None),
    Card("Page of Swords", "Skepticism, curiosity, observation", None),
    Card("Knight of Swords", "Honesty, truth, courage", None),
    Card("Queen of Swords", "Intelligence, clarity, wit", None),
    Card("King of Swords", "Justice, power, leadership", None),
    Card("Ace of Pentacles", "Prosperity, abundance, security", None),
    Card("Two of Pentacles", "Flexibility, balance, multitasking", None),
    Card("Three of Pentacles", "Teamwork, craftsmanship, learning", None),
    Card("Four of Pentacles", "Stability, conservation, control", None),
    Card("Five of Pentacles", "Poverty, loss, exclusion", None),
    Card("Six of Pentacles", "Generosity, sharing, charity", None),
    Card("Seven of Pentacles", "Patience, hard work, success", None),
    Card("Eight of Pentacles", "Focus, skill, apprenticeship", None),
    Card("Nine of Pentacles", "Wealth, luxury, comfort", None),
    Card("Ten of Pentacles", "Legacy, family, inheritance", None),
    Card("Page of Pentacles", "Curiosity, exploration, learning", None),
    Card("Knight of Pentacles", "Patience, hard work, discipline", None),
    Card("Queen of Pentacles", "Nurturing, comfort, resourcefulness", None),
    Card("King of Pentacles", "Wealth, stability, generosity", None)
])


print(f"\nThese cards represent the {category} portion of your life.")


def draw_card():

    random.shuffle(cards)
    card = random.choice(cards)
    cards.popleft()

    if random.randint(0, 1) == 0:
        card.orientation = "Upside down"
    else:
        card.orientation = "Facing up"

    print("You have drawn the card:", card.name)
    print("Meaning:", card.meaning)
    print("Orientation:", card.orientation)
    print("Orientation meaning:", card.ORIENTATION_MEANINGS[card.orientation])

for i in range(3):
    tense = ["Past:", "Present:", "Future:"]
    print(f"\n[Card {i+1}]\n{tense[i]}")
    draw_card()
