import random
from collections import deque

class Card:
    def __init__(self, name, meaning, orientation = None):
        self.name = name
        self.meaning = meaning
        self.orientation = None


    ORIENTATION_MEANINGS = {
        "Facing up": "Positive, or what is asked for is coming to pass.",
        "Upside down": "Negative, or what is asked for is not coming to pass."
    }


category = input("What are you asking the tarot cards: ")


cards = deque([
    Card("The Fool", "New beginnings, spontaneity, trust in the universe"),
    Card("The Magician", "Power, concentration, resourcefulness"),
    Card("The High Priestess", "Intuition, mystery, inner knowledge"),
    Card("The Empress", "Abundance, fertility, femininity"),
    Card("The Emperor", "Authority, structure, protection"),
    Card("The Hierophant", "Tradition, beliefs, education"),
    Card("The Lovers", "Love, harmony, relationships"),
    Card("The Chariot", "Determination, courage, victory"),
    Card("Strength", "Courage, strength, determination"),
    Card("The Hermit", "Introspection, inner guidance, prudence"),
    Card("Wheel of Fortune", "Good luck, karma, destiny"),
    Card("Justice", "Justice, fairness, truth"),
    Card("The Hanged Man", "Sacrifice, change, reversal"),
    Card("Death", "Transformation, endings, rebirth"),
    Card("Temperance", "Moderation, balance, harmony"),
    Card("The Devil", "Temptation, materialism, addiction"),
    Card("The Tower", "Catastrophe, upheaval, unexpected change"),
    Card("The Star", "Hope, optimism, serenity"),
    Card("The Moon", "Illusion, fear, intuition"),
    Card("The Sun", "Enlightenment, happiness, vitality"),
    Card("Judgement", "Inner calling, absolution, awakening"),
    Card("The World", "Completion, success, journey's end"),
    Card("Ace of Wands", "Initiative, creativity, energy"),
    Card("Two of Wands", "Ambition, planning, courage"),
    Card("Three of Wands", "Exploration, expansion, growth"),
    Card("Four of Wands", "Celebration, stability, rest"),
    Card("Five of Wands", "Competition, conflict, ambition"),
    Card("Six of Wands", "Victory, success, pride"),
    Card("Seven of Wands", "Courage, perseverance, defense"),
    Card("Eight of Wands", "Speed, action, progress"),
    Card("Nine of Wands", "Resilience, strength, tenacity"),
    Card("Ten of Wands", "Overextension, burden, oppression"),
    Card("Page of Wands", "Innovation, exploration, enthusiasm"),
    Card("Knight of Wands", "Passion, adventure, impulsiveness"),
    Card("Queen of Wands", "Charisma, leadership, courage"),
    Card("King of Wands", "Authority, confidence, power"),
    Card("Ace of Cups", "Emotions, love, compassion"),
    Card("Two of Cups", "Connection, balance, harmony"),
    Card("Three of Cups", "Celebration, friendship, joy"),
    Card("Four of Cups", "Contemplation, introspection, apathy"),
    Card("Five of Cups", "Loss, regret, disappointment"),
    Card("Six of Cups", "Nostalgia, childhood, innocence"),
    Card("Seven of Cups", "Imagination, wishful thinking, choices"),
    Card("Eight of Cups", "Moving on, inner journey, journey"),
    Card("Nine of Cups", "Happiness, contentment, satisfaction"),
    Card("Ten of Cups", "Family, community, harmony"),
    Card("Page of Cups", "Inquisitiveness, creativity, imagination"),
    Card("Knight of Cups", "Romance, creativity, emotion"),
    Card("Queen of Cups", "Intuition, empathy, compassion"),
    Card("King of Cups", "Wisdom, diplomacy, calmness"),
    Card("Ace of Swords", "Truth, justice, clarity"),
    Card("Two of Swords", "Stalemate, inner conflict, indecision"),
    Card("Three of Swords", "Heartache, sorrow, pain"),
    Card("Four of Swords", "Rest, recuperation, contemplation"),
    Card("Five of Swords", "Defeat, humiliation, loss"),
    Card("Six of Swords", "Transition, moving on, healing"),
    Card("Seven of Swords", "Deception, thievery, cunning"),
    Card("Eight of Swords", "Restriction, imprisonment, confusion"),
    Card("Nine of Swords", "Anxiety, fear, worry"),
    Card("Ten of Swords", "Failure, defeat, end of a situation"),
    Card("Page of Swords", "Skepticism, curiosity, observation"),
    Card("Knight of Swords", "Honesty, truth, courage"),
    Card("Queen of Swords", "Intelligence, clarity, wit"),
    Card("King of Swords", "Justice, power, leadership"),
    Card("Ace of Pentacles", "Prosperity, abundance, security"),
    Card("Two of Pentacles", "Flexibility, balance, multitasking"),
    Card("Three of Pentacles", "Teamwork, craftsmanship, learning"),
    Card("Four of Pentacles", "Stability, conservation, control"),
    Card("Five of Pentacles", "Poverty, loss, exclusion"),
    Card("Six of Pentacles", "Generosity, sharing, charity"),
    Card("Seven of Pentacles", "Patience, hard work, success"),
    Card("Eight of Pentacles", "Focus, skill, apprenticeship"),
    Card("Nine of Pentacles", "Wealth, luxury, comfort"),
    Card("Ten of Pentacles", "Legacy, family, inheritance"),
    Card("Page of Pentacles", "Curiosity, exploration, learning"),
    Card("Knight of Pentacles", "Patience, hard work, discipline"),
    Card("Queen of Pentacles", "Nurturing, comfort, resourcefulness"),
    Card("King of Pentacles", "Wealth, stability, generosity")
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
