def tribonacci(signature, n):
    if n:
        result = signature.copy()

        if n<3:
            return result[0:n]

        for x in range(2,n-1):
            el = result[x-2]+result[x-1]+result[x]
            result.append(el)

        return result

    return []
