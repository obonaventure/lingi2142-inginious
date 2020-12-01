#bash example
FILE=/archive/answers.txt
feedback-result success
feedback-grade 100
feedback-msg -ae -m "Thanks for your submission. This submission is not graded but will serve as input for the discussion for the next lesson."
getinput @username >> ${FILE}
echo -n " | " >> ${FILE}
echo -n " Solution | "  >> ${FILE}
getinput q >> ${FILE}

