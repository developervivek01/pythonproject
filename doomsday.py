
"""
Avengers: Doomsday 
"""

import json
import os

PROGRESS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "watch_progress.json")

WATCHLIST = [
    # --- Essential ---
    {
        "title": "Loki",
        "year": "2021",
        "type": "Series (S1)",
        "tier": "essential",
        "reason": "Introduces the Sacred Timeline and the multiverse -- the whole reason "
                  "multiple realities now collide in Doomsday.",
    },
    {
        "title": "Doctor Strange in the Multiverse of Madness",
        "year": "2022",
        "type": "Movie",
        "tier": "essential",
        "reason": "First real dive into parallel Earths and the Illuminati, including an "
                  "alternate Reed Richards -- groundwork for the Fantastic Four crossing over.",
    },
    {
        "title": "Loki",
        "year": "2023",
        "type": "Series (S2)",
        "tier": "essential",
        "reason": "Resolves the TVA storyline and branches the timelines wide open, setting "
                  "the multiversal stage Doomsday plays out on.",
    },
    {
        "title": "Deadpool & Wolverine",
        "year": "2024",
        "type": "Movie",
        "tier": "essential",
        "reason": "Officially folds the old X-Men film universe into the MCU multiverse -- why "
                  "X-Men characters like Gambit can now stand next to the Avengers.",
    },
    {
        "title": "Captain America: Brave New World",
        "year": "2025",
        "type": "Movie",
        "tier": "essential",
        "reason": "Sam Wilson steps up as the new Captain America, confirmed to lead the team "
                  "in Doomsday.",
    },
    {
        "title": "Thunderbolts*",
        "year": "2025",
        "type": "Movie",
        "tier": "essential",
        "reason": "Yelena, Bucky, Red Guardian, Ghost, and US Agent become the New Avengers -- "
                  "all confirmed for Doomsday's roster.",
    },
    {
        "title": "The Fantastic Four: First Steps",
        "year": "2025",
        "type": "Movie",
        "tier": "essential",
        "reason": "Origin of Reed Richards, Sue Storm, Johnny Storm, and Ben Grimm, whose world "
                  "collides with the main MCU timeline in Doomsday.",
    },
    # --- Recommended ---
    {
        "title": "Shang-Chi and the Legend of the Ten Rings",
        "year": "2021",
        "type": "Movie",
        "tier": "recommended",
        "reason": "Shang-Chi is confirmed to appear in Doomsday -- worth knowing his backstory.",
    },
    {
        "title": "Black Panther: Wakanda Forever",
        "year": "2022",
        "type": "Movie",
        "tier": "recommended",
        "reason": "Sets up Namor and the state of Wakanda, both part of Doomsday's three-universe setup.",
    },
    {
        "title": "Ant-Man and the Wasp: Quantumania",
        "year": "2023",
        "type": "Movie",
        "tier": "recommended",
        "reason": "Scott Lang's Quantum Realm arc, and the Kang storyline that Doom's casting "
                  "replaced -- useful context for why the villain plan changed.",
    },
    {
        "title": "What If...?",
        "year": "2021-2024",
        "type": "Series (S1-S3)",
        "tier": "recommended",
        "reason": "Explores alternate universes and variants across the multiverse in bite-sized form.",
    },
    # --- Optional / legacy ---
    {
        "title": "Iron Man",
        "year": "2008",
        "type": "Movie",
        "tier": "optional",
        "reason": "Not required, but seeing RDJ's original Tony Stark makes his reveal as "
                  "Doctor Doom land much harder.",
    },
    {
        "title": "Avengers: Infinity War / Endgame",
        "year": "2018-2019",
        "type": "Movie",
        "tier": "optional",
        "reason": "The Russo brothers' last Avengers outings -- same directors, same "
                  "large-ensemble structure returning for Doomsday.",
    },
    {
        "title": "X-Men: Days of Future Past",
        "year": "2014",
        "type": "Movie",
        "tier": "optional",
        "reason": "Classic Fox X-Men time-travel story; good legacy background for the X-Men "
                  "characters now entering the MCU.",
    },
]

TIER_ORDER = ["essential", "recommended", "optional"]
TIER_LABELS = {
    "essential": "ESSENTIAL -- watch these",
    "recommended": "RECOMMENDED -- adds context",
    "optional": "OPTIONAL -- bonus legacy lore",
}


def item_key(item):
    """Unique id for an entry (title differs across Loki seasons, etc.)."""
    return f"{item['title']} ({item['year']})"


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return set(json.load(f))
        except (json.JSONDecodeError, OSError):
            return set()
    return set()


def save_progress(watched):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(sorted(watched), f, indent=2)


def display_list(watched, tier_filter=None):
    print()
    numbered = enumerate(WATCHLIST, start=1)
    entries = [(i, item) for i, item in numbered if tier_filter is None or item["tier"] == tier_filter]

    current_tier = None
    for i, item in entries:
        if item["tier"] != current_tier:
            current_tier = item["tier"]
            print(f"\n--- {TIER_LABELS[current_tier]} ---")
        mark = "[x]" if item_key(item) in watched else "[ ]"
        print(f" {i:>2}. {mark} {item['title']} ({item['year']}) - {item['type']}")
        print(f"        -> {item['reason']}")
    print()


def search_title(keyword):
    keyword = keyword.lower().strip()
    results = [item for item in WATCHLIST if keyword in item["title"].lower()]
    if not results:
        print(f'\nNo matches for "{keyword}".\n')
        return
    print()
    for item in results:
        print(f"- {item['title']} ({item['year']}) [{TIER_LABELS[item['tier']]}]")
        print(f"    -> {item['reason']}")
    print()


def toggle_watched(watched, number_str):
    try:
        idx = int(number_str)
        if not (1 <= idx <= len(WATCHLIST)):
            raise ValueError
    except ValueError:
        print("\nEnter a valid number from the list (use option 1 to see numbers).\n")
        return
    item = WATCHLIST[idx - 1]
    key = item_key(item)
    if key in watched:
        watched.remove(key)
        print(f"\nMarked as NOT watched: {key}\n")
    else:
        watched.add(key)
        print(f"\nMarked as watched: {key}\n")
    save_progress(watched)


def show_progress(watched):
    total = len(WATCHLIST)
    done = sum(1 for item in WATCHLIST if item_key(item) in watched)
    essential_total = sum(1 for item in WATCHLIST if item["tier"] == "essential")
    essential_done = sum(1 for item in WATCHLIST if item["tier"] == "essential" and item_key(item) in watched)
    pct = (done / total * 100) if total else 0
    print(f"\nOverall progress: {done}/{total} watched ({pct:.0f}%)")
    print(f"Essential viewing: {essential_done}/{essential_total} watched")
    if essential_done == essential_total:
        print("You're fully ready for Avengers: Doomsday!\n")
    else:
        print("Prioritize the ESSENTIAL list before December 18, 2026.\n")


def main():
    watched = load_progress()
    print("=" * 60)
    print(" AVENGERS: DOOMSDAY -- REQUIRED VIEWING GUIDE")
    print(" In theaters December 18, 2026")
    print("=" * 60)

    menu = """
1. Show full watch order
2. Show essential-only list
3. Search for a title
4. Mark a title as watched / unwatched (enter its number)
5. Show my progress
6. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_list(watched)
        elif choice == "2":
            display_list(watched, tier_filter="essential")
        elif choice == "3":
            keyword = input("Search title: ")
            search_title(keyword)
        elif choice == "4":
            display_list(watched)
            number_str = input("Enter the number to toggle watched: ")
            toggle_watched(watched, number_str)
        elif choice == "5":
            show_progress(watched)
        elif choice == "6":
            print("\nEnjoy the movie!\n")
            break
        else:
            print("\nPlease choose a number between 1 and 6.\n")


if __name__ == "__main__":
    main()