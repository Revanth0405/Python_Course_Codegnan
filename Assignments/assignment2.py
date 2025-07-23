import re
from collections import Counter

def input_messages():
    num = int(input("Enter the number of messages: "))
    messages = []
    for _ in range(num):
        msg = input()
        if ':' in msg:
            messages.append(msg.strip())
        else:
            print("Invalid format. Message skipped.")
    return messages

def parse_messages(messages):
    parsed = []
    for msg in messages:
        try:
            name, message = msg.split(":", 1)
            parsed.append((name.strip(), message.strip()))
        except ValueError:
            pass  # Skip malformed messages
    return parsed

# ANALYSIS FUNCTIONS

def total_messages(messages):
    print(f"Total messages: {len(messages)}")

def unique_users(parsed):
    users = {user for user, _ in parsed}
    print(f"Unique users in the chat: {users}")

def total_words(parsed):
    total = sum(len(message.split()) for _, message in parsed)
    print(f"Total words in the chat: {total}")

def average_words(parsed):
    total = sum(len(message.split()) for _, message in parsed)
    avg = total / len(parsed) if parsed else 0
    print(f"Average words per message: {round(avg, 2)}")

def longest_message(messages):
    longest = max(messages, key=lambda m: len(m))
    print(f"Longest message: \"{longest}\"")

def most_active_user(parsed):
    counter = Counter(user for user, _ in parsed)
    user, count = counter.most_common(1)[0]
    print(f"Most active user: {user} ({count} messages)")

def message_count_user(parsed):
    name = input("Enter user name: ").strip()
    count = sum(1 for user, _ in parsed if user.lower() == name.lower())
    print(f"Messages sent by {name}: {count}")

def most_frequent_word_user(parsed):
    name = input("Enter user name: ").strip()
    words = []
    for user, message in parsed:
        if user.lower() == name.lower():
            words += re.findall(r'\b\w+\b', message.lower())
    if words:
        common_word, _ = Counter(words).most_common(1)[0]
        print(f'Most frequent word used by {name}: "{common_word}"')
    else:
        print(f"No messages by {name}")

def first_last_message(parsed):
    name = input("Enter user name: ").strip()
    user_msgs = [f"{user}: {msg}" for user, msg in parsed if user.lower() == name.lower()]
    if user_msgs:
        print(f'First message by {name}: "{user_msgs[0]}"')
        print(f'Last message by {name}: "{user_msgs[-1]}"')
    else:
        print(f"No messages by {name}")

def check_user_present(parsed):
    name = input("Enter user name: ").strip()
    users = {user.lower() for user, _ in parsed}
    if name.lower() in users:
        print(f"User '{name}' is present in the chat.")
    else:
        print(f"User '{name}' not found in the chat.")

def repeated_words(parsed):
    all_words = [word.lower() for _, msg in parsed for word in re.findall(r'\b\w+\b', msg)]
    repeated = {word for word, count in Counter(all_words).items() if count > 1}
    print(f"Common repeated words: {repeated}")

def longest_avg_message(parsed):
    user_lengths = {}
    user_counts = {}
    for user, msg in parsed:
        word_count = len(msg.split())
        user_lengths[user] = user_lengths.get(user, 0) + word_count
        user_counts[user] = user_counts.get(user, 0) + 1
    avg_lengths = {u: user_lengths[u] / user_counts[u] for u in user_lengths}
    user = max(avg_lengths, key=avg_lengths.get)
    print(f"User with longest average message: {user} (avg {round(avg_lengths[user], 2)} words)")

def mention_count(parsed):
    name = input("Enter name to check mentions: ").strip().lower()
    count = sum(1 for _, msg in parsed if name in msg.lower())
    print(f"Messages mentioning '{name}': {count}")

def remove_duplicates(messages):
    unique_msgs = list(dict.fromkeys(messages))
    print(f"Unique messages count: {len(unique_msgs)}")
    for msg in unique_msgs:
        print(msg)

def sort_messages(messages):
    sorted_msgs = sorted(messages, key=lambda x: x.lower())
    print("Messages sorted A-Z:")
    for msg in sorted_msgs:
        print(msg)

def extract_questions(messages):
    questions = [msg for msg in messages if '?' in msg]
    print("Questions in the chat:")
    for q in questions:
        print(q)

def reply_ratio(parsed):
    user1 = input("Enter sender: ").strip().lower()
    user2 = input("Enter replier: ").strip().lower()
    count = 0
    prev_user = None
    for user, msg in parsed:
        if prev_user == user1 and user == user2:
            count += 1
        prev_user = user
    print(f"Reply ratio from {user2.capitalize()} to {user1.capitalize()}: {count} replies")

def deleted_messages(parsed):
    count = sum(1 for _, msg in parsed if msg.strip().lower() == "this message was deleted")
    print(f"Deleted messages found: {count}")

# MAIN MENU

def main():
    messages = input_messages()
    parsed = parse_messages(messages)

    options = {
        1: lambda: total_messages(messages),
        2: lambda: unique_users(parsed),
        3: lambda: total_words(parsed),
        4: lambda: average_words(parsed),
        5: lambda: longest_message(messages),
        6: lambda: most_active_user(parsed),
        7: lambda: message_count_user(parsed),
        8: lambda: most_frequent_word_user(parsed),
        9: lambda: first_last_message(parsed),
        10: lambda: check_user_present(parsed),
        11: lambda: repeated_words(parsed),
        13: lambda: longest_avg_message(parsed),
        14: lambda: mention_count(parsed),
        15: lambda: remove_duplicates(messages),
        16: lambda: sort_messages(messages),
        17: lambda: extract_questions(messages),
        18: lambda: reply_ratio(parsed),
        19: lambda: deleted_messages(parsed),
    }

    while True:
        print("\nChoose an analysis option (1–19, 0 to exit):")
        choice = int(input())
        if choice == 0:
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

#Output
# Enter the number of messages: 6
# Alice: Good morning!
# Bob: Morning Alice!
# Charlie: Morning everyone!
# Alice: Hope you all have a great day?
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend?

# Choose an analysis option (1–19, 0 to exit):
# 1
# Total messages: 6

# Choose an analysis option (1–19, 0 to exit):
# 2
# Unique users in the chat: {'Alice', 'Charlie', 'Bob'}

# Choose an analysis option (1–19, 0 to exit):
# 3
# Total words in the chat: 22

# Choose an analysis option (1–19, 0 to exit):
# 4
# Average words per message: 3.67

# Choose an analysis option (1–19, 0 to exit):
# 5
# Longest message: "Charlie: Let's plan something fun this weekend?"

# Choose an analysis option (1–19, 0 to exit):
# 6
# Most active user: Alice (2 messages)

# Choose an analysis option (1–19, 0 to exit):
# 7
# Enter user name: Alice
# Messages sent by Alice: 2

# Choose an analysis option (1–19, 0 to exit):
# 7
# Enter user name: Bob
# Messages sent by Bob: 2

# Choose an analysis option (1–19, 0 to exit):
# 7
# Enter user name: Charlie
# Messages sent by Charlie: 2

# Choose an analysis option (1–19, 0 to exit):
# 8
# Enter user name: Alice
# Most frequent word used by Alice: "good"

# Choose an analysis option (1–19, 0 to exit):
# 9
# Enter user name: alice
# First message by alice: "Alice: Good morning!"
# Last message by alice: "Alice: Hope you all have a great day?"

# Choose an analysis option (1–19, 0 to exit):
# 10
# Enter user name: xyz
# User 'xyz' not found in the chat.

# Choose an analysis option (1–19, 0 to exit):
# 11
# Common repeated words: {'alice', 'you', 'morning'}

# Choose an analysis option (1–19, 0 to exit):
# 13
# User with longest average message: Alice (avg 4.5 words)

# Choose an analysis option (1–19, 0 to exit):
# 14
# Enter name to check mentions: Bob
# Messages mentioning 'bob': 0

# Choose an analysis option (1–19, 0 to exit):
# 15
# Unique messages count: 6
# Alice: Good morning!
# Bob: Morning Alice!
# Charlie: Morning everyone!
# Alice: Hope you all have a great day?
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend?

# Choose an analysis option (1–19, 0 to exit):
# 16
# Messages sorted A-Z:
# Alice: Good morning!
# Alice: Hope you all have a great day?
# Bob: Morning Alice!
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend?
# Charlie: Morning everyone!

# Choose an analysis option (1–19, 0 to exit):
# 17
# Questions in the chat:
# Alice: Hope you all have a great day?
# Charlie: Let's plan something fun this weekend?

# Choose an analysis option (1–19, 0 to exit):
# 18
# Enter sender: Charlie
# Enter replier: Alice
# Reply ratio from Alice to Charlie: 0 replies

# Choose an analysis option (1–19, 0 to exit):
# 19
# Deleted messages found: 0

# Choose an analysis option (1–19, 0 to exit):
# 0

# === Code Execution Successful ===