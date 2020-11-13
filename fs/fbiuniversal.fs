// NAME : FBI Universal Control Numbers
// URL  : https://open.kattis.com/problems/fbiuniversal
// =============================================================================
// Problem involving string parsing, character substitutions, conversion between
// base 10 and base 27, computation and validation of a 'check digit', and then
// printing results for valid strings.
// =============================================================================

open System

let disambiguate ch =
    // Replace an ambiguous character with the determined 'correct' one. This is done
    // because some characters are not easily distinguishable from related ones.
    match ch with
        | 'B' -> '8'
        | 'G' -> 'C'
        | 'I' -> '1'
        | 'O' -> '0'
        | 'Q' -> '0'
        | 'S' -> '5'
        | 'U' -> 'V'
        | 'Y' -> 'V'
        | 'Z' -> '2'
        | _ -> ch

let toBase10 ch =
    match ch with
        | '0' -> 0
        | '1' -> 1
        | '2' -> 2
        | '3' -> 3
        | '4' -> 4
        | '5' -> 5
        | '6' -> 6
        | '7' -> 7
        | '8' -> 8
        | '9' -> 9
        | 'A' -> 10
        | 'C' -> 11
        | 'D' -> 12
        | 'E' -> 13
        | 'F' -> 14
        | 'H' -> 15
        | 'J' -> 16
        | 'K' -> 17
        | 'L' -> 18
        | 'M' -> 19
        | 'N' -> 20
        | 'P' -> 21
        | 'R' -> 22
        | 'T' -> 23
        | 'V' -> 24
        | 'W' -> 25
        | 'X' -> 26
        | _ -> -1

let toBase27 d =
    match d with
        | 0 -> '0'
        | 1 -> '1'
        | 2 -> '2'
        | 3 -> '3'
        | 4 -> '4'
        | 5 -> '5'
        | 6 -> '6'
        | 7 -> '7'
        | 8 -> '8'
        | 9 -> '9'
        | 10 -> 'A'
        | 11 -> 'C'
        | 12 -> 'D'
        | 13 -> 'E'
        | 14 -> 'F'
        | 15 -> 'H'
        | 16 -> 'J'
        | 17 -> 'K'
        | 18 -> 'L'
        | 19 -> 'M'
        | 20 -> 'N'
        | 21 -> 'P'
        | 22 -> 'R'
        | 23 -> 'T'
        | 24 -> 'V'
        | 25 -> 'W'
        | 26 -> 'X'
        | _ -> 'Z'

let checkDigitFromArr (a : int list) =
    // Calculate the check digit based on an array of base 10 digits. This is a formula
    // specified in the problem description and simply needs to be worked out.
    (2*a.[0] + 4*a.[1] + 5*a.[2] + 7*a.[3] + 8*a.[4] + 10*a.[5] + 11*a.[6] + 13*a.[7]) % 27

let ucnToCheckDigit ucn =
    // Orchestrate the parsing, conversion, and calculation of the UCN into the check
    // digit. This is used to check the validity of the input case.
    ucn |> Seq.toList |> List.map toBase10 |> checkDigitFromArr |> toBase27

let ucnToBase10 ucn =
    let digits = Seq.toList ucn |> List.map toBase10 |> List.map int64
    Seq.fold (fun acc elem -> (acc + (digits.[7-elem] * (pown 27L elem)))) 0L [7..-1..0]

let solve (line : string) =
    let splits = line.Split([|' '|])
    let case = splits.[0]
    let ucn = splits.[1]
    let check = ucnToCheckDigit ucn
    let valid = check = ucn.[8]
    match valid with
        | true -> case + " " + (ucnToBase10 ucn |> string)
        | false -> case + " " + "Invalid"

[<EntryPoint>]
let main argv =
    let cases = Console.ReadLine() |> int
    [0..cases-1]
    |> Seq.map (fun x -> Console.ReadLine())
    |> Seq.map solve
    |> Seq.iter (function x -> printfn "%s" x)
    0
