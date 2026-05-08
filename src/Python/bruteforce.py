import sys
import random
import hashlib

def simulate_brute_force(target_hash):
            common_passwords = [
            "123456", "password", "123456789", "qwerty", "12345678", "12345", "1234567", "password123", "1234567890", "1234",
            "admin", "p@ssword", "root", "111111", "monkey", "sunshine", "iloveyou", "letmein", "secret", "football",
            "dragon", "master", "shadow", "hunter", "superman", "batman", "killer", "matrix", "hacker", "fsociety",
            "welcome", "login", "guest", "access", "system", "security", "server", "network", "firewall", "database",
            "000000", "123123", "654321", "987654321", "password1", "pass123", "abc123", "qazwsx", "wsxedc", "edcrfv",
            "chelsea", "arsenal", "liverpool", "united", "barcelona", "madrid", "soccer", "baseball", "basketball", "hockey",
            "charles", "george", "thomas", "william", "alexander", "nicholas", "matthew", "andrew", "daniel", "robert",
            "jennifer", "jessica", "michelle", "amanda", "ashley", "sarah", "stephanie", "heather", "nicole", "elizabeth",
            "princess", "angel", "sweetie", "honey", "cookie", "maggie", "charlie", "bailey", "lucky", "buster",
            "laptop", "computer", "keyboard", "monitor", "iphone", "android", "windows", "linux", "ubuntu", "kali", "elliot",
            "alderson", "elliotalderson", "verstappen", "hamilton", "starwars", "avengers", "pokemon", "superstar", "freedom", "awesome",
            "keyboard", "asdfghjk", "mnbvcxz", "1q2w3e4r", "password!", "P@ssw0rd1", "user1234", "test1234", "admin123", "manager",
            "spring2024", "summer24", "winter25", "january", "monday", "coffee", "whiskey", "tequila", "beer123", "smoke",
            "quantum", "entropy", "algorithm", "localhost", "127.0.0.1", "sysadmin", "database1", "oracle", "cisco123", "security!",
            "beowulf", "ragnarok", "anubis", "zeus123", "olympus", "viking", "sparta", "gladiator", "phoenix", "valhalla",
            "carpediem", "mementomori", "cogitoergo", "fortuna", "virtue", "justice", "liberty", "victory", "champion", "winner"
        ]

            print(f"\033[1;33m[!] INITIALIZING BRUTE FORCE ATTACK ON HASH: {target_hash}\033[0m")
            time.sleep(1)

            for password in common_passwords:
                sys.stdout.write(f"\r\033[1;34m[*] TRYING:\033[0m {password:<15}")
                sys.stdout.flush()
                
                time.sleep(random.uniform(0.3, 0.8))
                
                guess_hash = hashlib.md5(password.encode()).hexdigest()
                
                if guess_hash == target_hash:
                    print(f"\n\n\033[1;32m[+] MATCH FOUND!\033[0m")
                    print(f"\033[1;32m[+] PASSWORD:\033[0m {password}")
                    return
            
            print(f"\n\033[1;31m[-] ATTACK FAILED: Password not in dictionary.\033[0m")

target = "6f52550186105d6a2f7c006769062947" 
simulate_brute_force(target)