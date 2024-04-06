
I'd like to organise something similar as a mix between tiny chess bot tourney and hash code at some point, perhaps stuff that involves score maximisation but in a competitive/zero-sum environment (direct showdowns are just too fun not to have, imo, but "singleplayer" is still good too so idk), so more go's territory score than chess's checkmates

(I do think "static" optimisation problems like hash code, where the problem is "just" the search space, are far less interesting than "reactive" optimisation problems, where the search space is huge, yes, but your approach to it is generally influenced by something out of your control, hence multiplayer being great here, because the other player/bot won't let you play your "perfect" game most of the time)

so, for example, little goban (9x9, perhaps) can be a viable target, especially if we throw in some other constraint (memory/thread limits, code size, binary size, etc), or something where the scoring is nonlinear, such as best of worst scores (so multiple scores per player, rank only the worst) or something with a "greed" loss condition such as need money to buy points to win but whoever has the most money automatically loses, or a separate meter for "corruption" etc, or simply "whoever wins gets overgrown by the others who then have to turn spinner themselves to decide the winner from there, so who can overturn the rest is the winner be that being the last competitor or beating a coalition" which sells like a really fun one (kinda reverse RCV where the most popular that didn't secure majority gets eliminated rather than the least) which I think could be real interesting to solve (kinda anarcho monarchism the game a little)

let's call it kingmaker (or monarch maker for the alteration at expense to a classic phrase, though more searchable without the ambiguity)

in the worst case, we can stack these, ranked by where you fall behind, then whoever has fallen behind in scope that beats all remaining others combined wins, so imagine a simple swipe left right game, we have food, money, army, and "popular institutions"~~media bc religion is just organised media~~, so player A has 3 of each but fife is




## card game

take a deck of cards, if you have more than 4 players you may want a second deck (remove an entire suite if you wish to avoid ties)
shuffle the deck
deal each player an equal share of the cards
have the players stack each of their suites
now for scoring, that's right, game's coming to an end, this is just a demo
for each suite, rank the players, choose between you to either rank based on number of cards or sum of cards, you may turn this into a negotiation game and do each suite independently
declare your ranks for each suite (you do not need to show your cards)
if a player is rank 1 in more than half of the suites (3+ or 2+ if a suite was removed) they have won
if a player has rank 1 in half of the suites (in case of an even number) they have not won
if the game has not been won yet, eliminate whoever is the top player (rank 1 in the most suites, in case of ties, compare rank 2 in most suites, etc)
repeat above until someone has rank 1 of the remaining players in more than half of suites, whereupon the game has been won
