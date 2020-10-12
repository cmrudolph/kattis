// NAME : ASCII Addition
// URL  : https://open.kattis.com/problems/asciiaddition
// =============================================================================
// Not a difficult problem to understand. Lots of array extraction and
// transformation. First "real" problem done in F#, so language learning
// curve applied.
// =============================================================================

open System

let zero = ["xxxxx";"x...x";"x...x";"x...x";"x...x";"x...x";"xxxxx"]
let one = ["....x";"....x";"....x";"....x";"....x";"....x";"....x"]
let two = ["xxxxx";"....x";"....x";"xxxxx";"x....";"x....";"xxxxx"]
let three = ["xxxxx";"....x";"....x";"xxxxx";"....x";"....x";"xxxxx"]
let four = ["x...x";"x...x";"x...x";"xxxxx";"....x";"....x";"....x"]
let five = ["xxxxx";"x....";"x....";"xxxxx";"....x";"....x";"xxxxx"]
let six = ["xxxxx";"x....";"x....";"xxxxx";"x...x";"x...x";"xxxxx"]
let seven = ["xxxxx";"....x";"....x";"....x";"....x";"....x";"....x"]
let eight = ["xxxxx";"x...x";"x...x";"xxxxx";"x...x";"x...x";"xxxxx"]
let nine = ["xxxxx";"x...x";"x...x";"xxxxx";"....x";"....x";"xxxxx"]
let plus = [".....";"..x..";"..x..";"xxxxx";"..x..";"..x..";"....."]

let getConsoleInputSeq argv =
    (fun _ -> Console.ReadLine())
    |> Seq.initInfinite
    |> Seq.takeWhile ((<>) null)

let testInputSeq = seq {
    yield "....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx"
    yield "....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x"
    yield "....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x"
    yield "....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x"
    yield "....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x"
    yield "....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x"
    yield "....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx"
}

let singleDigitToInt digit =
    match digit with
    | x when x = zero -> 0
    | x when x = one -> 1
    | x when x = two -> 2
    | x when x = three -> 3
    | x when x = four -> 4
    | x when x = five -> 5
    | x when x = six -> 6
    | x when x = seven -> 7
    | x when x = eight -> 8
    | x when x = nine -> 9
    | _ -> -1

let singleIntToDigit intVal =
    match intVal with
    | 0 -> zero
    | 1 -> one
    | 2 -> two
    | 3 -> three
    | 4 -> four
    | 5 -> five
    | 6 -> six
    | 7 -> seven
    | 8 -> eight
    | 9 -> nine
    | _ -> plus

let intToDigits (intVal : int) =
    string intVal
    |> List.ofSeq
    |> List.map string
    |> List.map int
    |> List.map singleIntToDigit

let sumArrayDigits digits =
    List.fold (fun acc elem -> (acc * 10) + (singleDigitToInt elem)) 0 digits

let deriveSubMatrices numChars =
    // Identify the matrix coordinates for each digit. The digits occupy a fixed amount
    // of space, so we know the structures of the sub matrices
    List.map (fun x -> (x * 6, (x * 6) + 4)) [0..numChars - 1]

let extractDigitArray (digits : string list) (startIdx, endIdx) =
    [0..6] |> List.map (fun x -> digits.[x].[startIdx..endIdx])

let extractDigitArrays (digits : string list) subMatrices =
    // Extract each digit from the string array using a set of coordinates
    //List.map (fun (s, e) -> [0..6] |> List.map (fun x -> digits.[x].[s..e])) subMatrices
    List.map (extractDigitArray digits) subMatrices

let printJoinedArrayColumn (digits : string list list) col =
    [0..(digits.Length - 1)]
    |> List.map (fun x -> digits.[x].[col])
    |> String.concat "."
    |> printfn "%s"

let solve (digits : string list) =
    let numChars = ((digits.[0].Length) + 1) / 6
    let subMatrices = deriveSubMatrices numChars
    let digitArrays = extractDigitArrays digits subMatrices

    // Find the plus ASCII character and split on it. Each subarray contains a single
    // integer value that needs to be extracted later
    let plusIdx = List.findIndex (fun x -> x = plus) digitArrays

    // Interpret the digits as numbers and add them together
    let int1 = sumArrayDigits digitArrays.[..plusIdx - 1]
    let int2 = sumArrayDigits digitArrays.[plusIdx + 1..]
    let sum = int1 + int2
    let sumDigits = intToDigits sum

    // Print the final results
    [0..(sumDigits.[0].Length - 1)] |> List.iter (printJoinedArrayColumn sumDigits)

[<EntryPoint>]
let main argv =
    getConsoleInputSeq argv |> Seq.toList |> solve
    0
