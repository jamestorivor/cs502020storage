-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Information suggests to search for a theft that occured on July 28th, 2021
SELECT description
FROM crime_scene_reports
WHERE month = 7
AND year = 2021
AND day = 28
AND description LIKE '%theft%';

-- The description from crime_scene_reports suggests that there were interviews conducted and that should be looked at
SELECT *
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%thief%';

--Interviews conducted suggests that the thief exited the bakery within 10 minutes of the theft which occured at 10.15am according to the transcript
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 25
AND activity = 'exit';

-- Interviews conducted suggets that the thief withdrew money from the atm on the same day on Legget Street
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Interview suggests that the thief was on a call for less than a minute on the same day
SELECT caller,
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Finding out airport id to use in the flights table to search for flights out of fiftyville
SELECT id
FROM airports
WHERE city LIKE '%Fiftyville%';

-- Searching for the earliest flight out of fiftyville on the 29th of july 2021
SELECT *
FROM flights
WHERE origin_airport_id = 8
AND year = 2021
AND month = 7
AND day = 29
ORDER BY hour;

-- Searching for passport numbers of passengers who were on the earliest flight out of fiftyville
SELECT passport_number
FROM passengers
WHERE flight_id = 36;

--Searching people table for people who match all the descriptions of the passenger, who called on that day for less than 1 minute and who has a license plate that exited from the bakery within 10minutes of the crime and took the earliest flight out of fiftyville
SELECT name
FROM people
WHERE phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60)
AND passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id = 36)
AND license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute BETWEEN 15 AND 25);

-- Searching for id of people where there was a withdrawl of money on the same day of the theft
SELECT person_id
FROM bank_accounts
WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw');

-- Searching for a person who fits all the criterias
SELECT name
FROM people
WHERE name IN ('Sofia', 'Kelsey', 'Bruce')
AND id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw')
);

-- Searching for Bruce in people as Bruce fits all the
SELECT *
FROM people
WHERE name = 'Bruce';

-- Searching for the phone number of the accomplice
SELECT receiver
FROM phone_calls
WHERE caller = '(367) 555-5533'
AND year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Searching for the name of the accomplice who has the phone number (367) 555-5533
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';

-- Searching for the name of the airport that the thief fled to
SELECT *
FROM airports
WHERE id = 4;