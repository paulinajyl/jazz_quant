# Mathsy Jazz
Jazz is often misunderstood as elevator music. A bunch of of random notes played together that no one really understands — which in a sense is kind of true. But I want to try to understand what makes the randomness random, and explore how we can quantify the evolution of music. My project explores different analytical tools to analyze music, and aims to find musical insights through numbers and data.

### Quick Jazz 101
Jazz revolves around two key elements: the head and improvisation. The head, or main melody, anchors the piece, appearing at the beginning and end while providing a reference for musicians and listeners. Improvisation, the fun part, builds on the head, allowing musicians to explore rhythmic and harmonic variations in real-time. This spontaneous creativity fosters interaction, showcasing both individual expression and group cohesion (Nerd, 2013).

### Quantifying Jazz
My band teacher always emphasized playing within the key of the main melody, and varying rhythm more than trying to play a new note. Hence I first found ways to quantify pitch and rhythm in music.
1. Pitch: Markov chains
Jazz improvisation can be modelled using Markov chains, which predict note transitions probabilistically. These chains operate with a "memoryless" property, meaning each note is chosen based only on the previous one, which naively mirrors jazz’s spontaneity (Linskens, 2014).
2. Rhythm: IOI probabilities
Abrams (2023) analyzed jazz rhythm using inter-onset intervals (IOIs), measuring the time between accented notes. This method assumes rhythmic variations come from a probability distribution, enabling entropy calculations to quantify complexity.

While these methodologies provide insights into jazz structure, true improvisation goes beyond note-to-note transitions and rhythmic probabilities, incorporating an artist’s unique phrasing, motifs, and experience. But these simple tools serve as a starting point for analysis!

### Methods and Analysis
In my analysis, I first began with Canon in D by Pachelbel. I compared Pachabel to Hiromi Uehara’s arrangement, a famous contemporary pianist known for incorporating elements of jazz and rock into her compositions. Comparing classical to jazz showed the stark differences in each music’s properties. For example, the IOI histogram shows that Hiromi plays at a much faster pace (mean IOI 0.17) than Pachelbel (0.35), reflecting jazz’s rhythmic variation versus classical music’s regular phrasing. Despite overlapping note ranges, their rhythmic approaches differ significantly—an analysis that can also be applied to Moanin’ by Lee and other artists!

I analyzed jazz improvisational segments of Moanin’ by Art Blakey and the Jazz Messengers using YouTube data. The primary subject was trumpeter Lee Morgan, whose style serves as a reference point. 

I downloaded and standardized 8 of Morgan’s solos and 22 from other artists, ensuring consistency in key (F minor) and tempo (120 BPM). After isolating the solos with Soundverse.ai’s stemming tool, I converted the MP3 files to MIDI using Basic Pitch, an open-source audio-to-MIDI converter by Spotify, to extract musical patterns accurately.

MIDI files store performance data rather than actual sound, allowing precise analysis of note pitches, durations, and velocities. Using pretty_midi, I loaded and processed these MIDI files, extracting instrument tracks and musical features. Since MP3-to-MIDI conversion can introduce inaccuracies due to overlapping sounds, Basic Pitch was important in maintaining clarity, enabling a cleaner dataset for analyzing improvisational styles.

One of the key plots was the cumulative average of Lee’s notes and the ensemble average from the histogram. If extended beyond 20 minutes, the graph suggests Lee’s playing could converge to the ensemble average MIDI note, which is pretty cool! But it’s important to note that Jazz follows a head/solo structure where soloists return to key motifs to signal the end of their solo. In Moanin’, this ‘pre-head’ phrase, marking the solo’s conclusion, is F4-G4-Ab4-Db4 (MIDI: 65-67-68-61), reinforcing the F minor key, which could also explain the convergence towards 65.
