var allNotes= ['4C','4C#','4D','4D#','4E','4F','4F#','4G','4G#','4A','4A#','4B','5C','5C#','5D','5D#','5E','5F']
// check out onChange for the inputs
document.addEventListener("DOMContentLoaded", function(){
    window.synth = new Beep.Instrument().caymanSynth() //added this build class to beep.instrument.js
    window.synth.applyVoices( function(){ this.voices.push( 

        new Beep.Voice( this.note, this.audioContext )
            .setOscillatorType( 'sine' )
            .setAttackGain( 0.2 ),
    
        new Beep.Voice( this.note.hertz, this.audioContext )
            .setOscillatorType( 'triangle' )
            .setAttackGain( 0.02 )
            .setDelayDuration( 0.05 ),
    
        new Beep.Voice( this.note.hertz, this.audioContext )
            .setOscillatorType( 'sawtooth' )
            .setAttackGain( 0.02 ),
    
        new Beep.Voice( this.note.hertz, this.audioContext )
            .setOscillatorType( 'square' )
            .setAttackGain( 0.03 )
    )})
});

    // new Beep.Trigger('4C').addTriggerChar('a');
    // new Beep.Trigger('4C#').addTriggerChar('w');
    // new Beep.Trigger('4D').addTriggerChar('s');
    // new Beep.Trigger('4D#').addTriggerChar('e');
    // new Beep.Trigger('4E').addTriggerChar('d');
    // new Beep.Trigger('4F').addTriggerChar('f');
    // new Beep.Trigger('4F#').addTriggerChar('t');
    // new Beep.Trigger('4G').addTriggerChar('g');
    // new Beep.Trigger('4G#').addTriggerChar('y');
    // new Beep.Trigger('4A').addTriggerChar('h');
    // new Beep.Trigger('4A#').addTriggerChar('u');
    // new Beep.Trigger('4B').addTriggerChar('j');
    // new Beep.Trigger('5C').addTriggerChar('k');
    // new Beep.Trigger('5C#').addTriggerChar('o');
    // new Beep.Trigger('5D').addTriggerChar('l');
    // new Beep.Trigger('5D#').addTriggerChar('p');
    // new Beep.Trigger('5E').addTriggerChar(186);
    // new Beep.Trigger('5F').addTriggerChar(222);