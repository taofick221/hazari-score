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

    // Funny messages for each rank
    const funnyMessages = {
        1: [
            "KING OF BED 👑",
            "HAZARI BOSS 😎",
            "ROOMER SHAHENSHAH 👑",
            "AJKE TOR DIN 🔥",
            "MAIN CHARACTER 😎",
            "KING OF THE TABLE 👑",
            "BOSS LEVEL UNLOCKED 🔥",
            "TORI RAJOTTO 👑",
        ],

        2: [
            "USE MORE OIL 😂",
            "ALMOST HERO 😏",
            "RUNNER-UP WITH STYLE 🥈",
            "EKTU KOM HOISE 😭",
            "BOSS ER ASSISTANT 😎",
            "CHAMPION ER PICHONE 🏃",
            "SECOND HAND KING 😂",
            "KACHE GIYE FALTU 😭",
        ],

        3: [
            "BOU THAKBE NA 😂",
            "HALAR DARI NA 😭",
            "STILL BREATHING 💀",
            "TOR KI HOILO? 😂",
            "BHALO CHILISH 😭",
            "MID-LIFE CRISIS 💀",
            "GAME E ACHOS, KINTU KENO? 😂",
            "ALMOST USEFUL 😭",
        ],

        4: [
            "TEA SPONSOR ☕",
            "BASAY JAO 😂",
            "KI KORLI RE BHAI 💀",
            "TOR DIN SHESH 😭",
            "LAST BENCH LEGEND 😂",
            "POINT KOTHAY? 🔍",
            "HAZARI ER PATIENT 💀",
            "KICHU EKTA KOR BHAI 😭",
            "FREE TE KHELTESO 😂",
            "BHAI GHUMAO 😴",
        ],
    };

    function getRandomMessage(rank) {
        const messages = funnyMessages[rank];

        return messages[
            Math.floor(Math.random() * messages.length)
        ];
    }

    function updateFunnyMessages() {
        const rankTitles = document.querySelectorAll(".rank-title");

        rankTitles.forEach((title, index) => {
            const rank = index + 1;

            title.textContent = getRandomMessage(rank);
        });
    }

    function getValue(input) {
        return parseInt(input.value) || 0;
    }

    function totalScore() {
        let total = 0;

        inputs.forEach((input) => {
            total += getValue(input);
        });

        return total;
    }

    function validateRound() {
        const total = totalScore();

        if (total === ROUND_TOTAL) {
            infoBox.className = "alert alert-success";

            infoBox.innerHTML =
                `✅ Perfect! Total ${ROUND_TOTAL}`;

            saveButton.disabled = false;

            return;
        }

        if (total > ROUND_TOTAL) {
            infoBox.className = "alert alert-danger";

            infoBox.innerHTML =
                `❌ ${total - ROUND_TOTAL} points extra`;

            saveButton.disabled = true;

            return;
        }

        infoBox.className = "alert alert-warning";

        infoBox.innerHTML =
            `⚠️ Need ${ROUND_TOTAL - total} more points`;

        saveButton.disabled = true;
    }

    inputs.forEach((input) => {
        input.addEventListener("input", validateRound);
    });

    autoButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const index = Number(this.dataset.player);

            let total = 0;

            inputs.forEach((input, i) => {
                if (i !== index) {
                    total += getValue(input);
                }
            });

            const auto = Math.max(
                ROUND_TOTAL - total,
                0
            );

            inputs[index].value = auto;

            validateRound();
        });
    });

    // Random funny text every time the game page opens
    updateFunnyMessages();

    validateRound();
});