const ROUND_TOTAL = 360;

document.addEventListener("DOMContentLoaded", () => {

    const inputs = [
        document.getElementById("id_player1_score"),
        document.getElementById("id_player2_score"),
        document.getElementById("id_player3_score"),
        document.getElementById("id_player4_score"),
    ];

    const autoButtons = document.querySelectorAll(".auto-fill-btn");

    const saveButton = document.getElementById("save-round-btn");

    const infoBox = document.getElementById("auto-fill-info");

    if (!inputs[0]) {
        return;
    }

    function getValue(input) {
        return parseInt(input.value) || 0;
    }

    function totalScore() {

        let total = 0;

        inputs.forEach(input => {

            total += getValue(input);

        });

        return total;
    }

    function validateRound() {

        const total = totalScore();

        if (total === ROUND_TOTAL) {

            infoBox.className =
                "alert alert-success";

            infoBox.innerHTML =
                `✅ Perfect! Total ${ROUND_TOTAL}`;

            saveButton.disabled = false;

            return;
        }

        if (total > ROUND_TOTAL) {

            infoBox.className =
                "alert alert-danger";

            infoBox.innerHTML =
                `❌ ${total - ROUND_TOTAL} points extra`;

            saveButton.disabled = true;

            return;
        }

        infoBox.className =
            "alert alert-warning";

        infoBox.innerHTML =
            `⚠️ Need ${ROUND_TOTAL - total} more points`;

        saveButton.disabled = true;
    }

    inputs.forEach(input => {

        input.addEventListener(
            "input",
            validateRound
        );

    });

    autoButtons.forEach(button => {

        button.addEventListener(
            "click",
            function () {

                const index =
                    Number(this.dataset.player);

                let total = 0;

                inputs.forEach((input, i) => {

                    if (i !== index) {

                        total += getValue(input);

                    }

                });

                const auto =
                    Math.max(
                        ROUND_TOTAL - total,
                        0
                    );

                inputs[index].value = auto;

                validateRound();

            }
        );

    });

    validateRound();

});