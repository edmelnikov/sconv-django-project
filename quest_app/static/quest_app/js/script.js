// before reading this code, note that I've never programmed on JavaScript
// this code and the idea behind it are both fucking disgusting, but I don't really give a shit since I don't have enough time to make it any cleaner
// good luck figuring it out :)

document.getElementsByClassName("question 1")[0].style.display = 'block'; // show first question

let global_q_counter = 1; // global question counter
function show_next_q() {
    max_q_number = 16; // maximum number of questions

    // console.log(global_q_counter);

    // TODO: show a warning message when none of the radio buttons are pressed  

    if (global_q_counter < max_q_number) {
        let elements = document.getElementsByClassName("question " + global_q_counter.toString());
        if (elements.length > 0) {
            elements[0].style.display = 'none';  // hide current question
        }
        global_q_counter += 1;
        elements = document.getElementsByClassName("question " + global_q_counter.toString());
        if (elements.length > 0) {
            elements[0].style.display = 'block';  // show next question
            if (global_q_counter >= max_q_number) { // if we've reached the last question
                document.getElementsByClassName("button-next-q")[0].style.display = 'none'; // we hide the "next question" button
                document.getElementsByClassName("button-send")[0].style.display = 'block'; // and we show the "send" button     
            }
        }
    }
}