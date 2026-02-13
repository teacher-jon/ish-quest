// ==========================================
//  SUFFIXIA QUESTION DATABASE
// ==========================================
// This file contains all the word challenges for the game.
// It is organized by Level Index (0, 1, 2...).

const QUESTION_DATABASE = {
    // --- LEVEL 1: Pattern Matching (Basic Suffix Addition) ---
    // Focus: Simple "Noun + ish" construction.
    0: [
        { q: "Like a boy", a: "boyish" },
        { q: "Like a girl", a: "girlish" },
        { q: "Like a child", a: "childish" },
        { q: "Like a fool", a: "foolish" },
        { q: "Like a sheep", a: "sheepish" },
        { q: "Like a wolf", a: "wolfish" },
        { q: "Like a slug", a: "sluggish" },
        { q: "Like a devil", a: "devilish" },
        { q: "Like a fever", a: "feverish" },
        { q: "Like a baby", a: "babyish" }
    ],

    // --- LEVEL 2: Context Sentences (Fill in the Blank) ---
    // Focus: Using -ish words in context naturally.
    1: [
        { q: "It wasn't quite blue, just ____.", a: "bluish" },
        { q: "It felt damp, sort of ____.", a: "dampish" },
        { q: "I'll be there at two, or ____.", a: "twoish" },
        { q: "The leaf looked green, kind of ____.", a: "greenish" },
        { q: "Let's meet at seven, or ____.", a: "sevenish" },
        { q: "It tastes sweet, sort of ____.", a: "sweetish" },
        { q: "He looks forty, maybe ____.", a: "fortyish" },
        { q: "The tea is warm, kind of ____.", a: "warmish" },
        { q: "The car looks new, well, ____.", a: "newish" },
        { q: "The dog is fat, sort of ____.", a: "fattish" }
    ],

    // --- LEVEL 3: Grammar & Metalinguistics ---
    // Focus: Parts of speech, meaning analysis, and definitions.
    2: [
        { q: "Part of speech: Bookish", a: "adjective" },
        { q: "Part of speech: Ticklish", a: "adjective" },
        { q: "Meaning of -ish in 'Greenish'", a: "somewhat" },
        { q: "Meaning of -ish in 'English'", a: "origin" },
        { q: "Does 'Selfish' mean like or full of?", a: "full of" },
        { q: "Is 'Rubbish' an adjective?", a: "no" },
        { q: "Opposite of 'Selfish'", a: "selfless" },
        { q: "Does 'Childish' differ from 'Childlike'?", a: "yes" },
        { q: "Make 'Spain' an adjective", a: "spanish" },
        { q: "Make 'Dane' an adjective", a: "danish" }
    ]
};

// --- BOSS QUESTIONS (Meta/Rules) ---
const BOSS_DATABASE = [
    { q: "Does '-ish' usually turn a Noun into what?", a: "adjective" },
    { q: "If a word ends in 'e', do you keep it for -ish?", a: "no" },
    { q: "If a word has short vowel + consonant, do you double it?", a: "yes" },
    { q: "Which is correct: Blueish or Bluish?", a: "bluish" },
    { q: "Does -ish mean 'Exactly' or 'Approximately'?", a: "approximately" }
];
