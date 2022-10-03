# Herald of Code

A Discord Bot for setting up your own [Advent of Code](https://adventofcode.com) styled events!

![Inspired by this chat](inspiration.png)

The plan is to not need any scheduling or anything. So long as a problem is available, then if it's on/after the day that problem unlocks (default, consecutive days), that problem can be attempted (and its description can be shared). Multiple-stage problems will be handled later, probably at first by just setting up nested tables that get done in sequence, or by starting to do a branching paths approach later; much later, if we still want this, just thought it might be interesting for bigger events, though that might be branching paths rather than consecutive problems.

Users will use modern discord interactions and `/<command>` or such to request the problem description (just for them, not visible to anyone else) and their personal input (again, not visible to anyone else), and then be able to post their outputs (only visible when they got it correct, alongside their leaderboard position on this problem and for the event). They can also ask for the leaderboard in general, both for a problem and for an entire event. Past problems will be available, and events can be set to either unlock all problems at the start ("freestyle", like Project Euler) or (by default) unlock all at the end (so people can skip to the harder ones). Prior to this, you only unlock at the rate of completion, or when the problem is available, whichever comes later.

If Discord lets us present a menu, then we're able to populate that with the current events and problems, depending on what was asked for. When only one event is ongoing, we assume that one when asking for the problems, otherwise we show all events with their most-recently unlocked problem. Picking one will provide the description and input for said problem. Or they can look at the menu of past or freestyle events for them to pick from. For paginated problems, make sure to offer immediate "continue" or "start" options, and since it'll start from the most recent, offer a "skip to oldest" page, simialrly with menu of events (showing the most recently updated first).

While we may have standard AoC style problems with just a description and examples, we'll also have "scary code" problems where you must debug example code to get the right output. For the sake of people, we'll provide difficulty ratings, and by default we'll unlock from lowest to highest (on consecutive days).

Different events or stand-alone problems will be different TOML files in `./problems/`, such as `./problems/2022-swacktober.toml`.

Users will have all their secret inputs and expected outputs per problem as TOML files in `./users/<user>.toml`, no other information should need to be stored. Since this uses their Discord UUID it will be resistant to username changes, though we'll need a way to sync/rename for new accounts (such as if someone got hacked) --- not a high priority but it'd probably come up eventually.

In the AoC format, each person gets some secret, personal input for a problem. This either modifies it somehow, or provides the input to be run through the program.

I'm not fussed, so like SwackQuote, this will be something you're expected to run yourself, so have a separate bot per server. Sorry, I just don't need anything more complicated, but if you'd like to improve, feel free to fork it. Having per-server `./<server>/problems/` & `./<server>/users/` directories is a clean approach, if you want my recommendation.
