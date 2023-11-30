def prime_factorization(n: int) -> list:
    """
    Given an integer N, return a list of all the prime numbers,
      which when multiplied together, have a product of N.

    For example, 24 = 2^3 * 3, so for 24 we return [2,2,2,3]

    :param n: an integer greater than 0
    :return: a list of integers which are all prime
    """
    if n < 2:
        raise ValueError(f"Cannot perform prime factorization on an integer <2. Provided: {n}")

    # add 1 to make sure that we get the biggest possible
    # prime factor in our list of candidate primes
    primes = get_primes(n + 1)

    result = []

    # Every time we find a factor of our original number n, we can
    # add it to our result list, and divide it from the original number. This leaves
    # a new "target" number which is n / prime.
    # Example: If we were working with 24, we'd find that it divides by 2.
    # So 2 goes in our result list, and our new "target" is 12.
    # We will keep doing this until we find that our target number is itself a prime.
    target = n

    # We can stop searching for factors when the target number is itself a prime.
    while target not in primes:
        # try each of the primes in the list we requested above.
        for prime in primes:
            # does it divide evenly into target?
            if target % prime == 0:
                # found one! add it to the list of primes we found, and update
                # the current target value to reflect that we found a factor
                result.append(prime)
                target = target // prime

                # the "break" keyword says "quit the current loop", which is
                # going through all the primes. We want to start again at the first
                # prime number (2) when we search for factors in our new target.
                break
    # since we know target is a prime number (we just stopped the loop)
    # we need to be sure to add it to our result list.
    result.append(target)
    return result


def get_primes(max_number: int) -> list:
    """
    Return a list of all prime numbers less than or equal to max_number.
    (Reminder: a prime number is a whole number greater than 1 whose
    only factors are 1 and itself.)

    :param max_number: a positive integer greater than 2
    :return: an ordered list of numbers which are prime,
      all of which are less than or equal to max_number
    """
    # the first prime number is 2. if you
    # include 1 in this list (right now) then
    # this function will return that every number
    # is not prime, because 1 will divide into every
    # number evenly.
    if max_number < 2:
        raise ValueError(f"get_primes() only works for a positive integer >= 2. provided: {max_number}")

    known_primes = [2]

    # look at every integer less than or equal to n
    for candidate_prime in range(2, max_number + 1):

        # start by assuming that this candidate number is prime
        candidate_is_prime = True

        # try all the known the primes 2 < potential_factor < candidate_prime to
        # see if they divide evenly into candidate_prime.
        # if potential_factor divides evenly into candidate_prime, then candidate_prime is
        # not prime. try the next potential_factor.
        for potential_factor in known_primes:
            if candidate_prime % potential_factor == 0:
                # no remainder from modulo division: not prime!
                candidate_is_prime = False
                # break says "quit the loop, because we have
                # our answer already. no need to consider any
                # additional potential_factors."
                break

        # if you looked at all of those potential_factors, and didn't
        # find anything which divides into candidate_prime evenly, then
        # candidate_prime is prime and should be added to our known_primes.
        if candidate_is_prime:
            known_primes.append(candidate_prime)
    return known_primes


if __name__ == "__main__":
    for i in range(2, 1001):
        print(f"{i}: {prime_factorization(i)}")
