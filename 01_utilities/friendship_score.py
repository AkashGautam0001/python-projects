def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set("aeiou")

    score += len(shared_letters)*5
    score += len(vowels & shared_letters)*10
     
    return min(score, 100)

def run_friendship_score():
    print("❤️ Friendship Score ❤️")
    name1 = input("Enter name 1 : ").strip()
    name2 = input("Enter name 2 : ").strip()
    print(friendship_score(name1, name2))

run_friendship_score()