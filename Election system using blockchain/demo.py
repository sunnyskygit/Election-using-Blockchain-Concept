from blockchain import Blockchain

def main():
    chain1=Blockchain()
    chain2=Blockchain()
    
    

    candidate1=input('Enter first candidate name')
    candidate2=input('Enter second candidate name')
    cand1_votes=0
    cand2_votes=0
    voters_id=[101,102,103,104,105,106]
    no_of_voters=len(voters_id)
    print('no of voters:',no_of_voters)
    voted=[]
    while True:
        if voters_id==[]:
            print('voting is over')
            if cand1_votes>cand2_votes:
                print(f"{candidate1} won the election with {cand1_votes}")
                print(f"AND THE VOTES FOR {candidate1} ARE:")
                chain1.print_blockchain()
            elif cand2_votes>cand1_votes:
                print(f"{candidate2} won the election with {cand2_votes}")
                print(f"AND THE VOTES FOR {candidate2} ARE:")
                chain2.print_blockchain()
            elif cand1_votes==cand2_votes:
                print('tied!!')
                chain1.print_blockchain()
                chain2.print_blockchain()
            break
        else:
            voter=int(input('Enter your Id:'))
            if voter in voted:
                print('you already voted')
            else:
                if voter in voters_id:
                    
                    print(f"1.{candidate1}\n2.{candidate2}")
                    choice=int(input('Enter your choice'))
                    if choice==1:
                        chain1.add_block(voter)
                        cand1_votes+=1
                        print(f"you voted {candidate1}")
                    elif choice==2:
                        chain2.add_block(voter)
                        cand2_votes+=1
                        print(f"you voted {candidate2}")
                    voters_id.remove(voter)
                    voted.append(voter)
                else:
                    print('you are not allowed to vote')
if __name__ == '__main__':
	main()