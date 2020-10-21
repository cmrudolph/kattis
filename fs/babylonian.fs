// NAME : Babylonian Numbers
// URL  : https://open.kattis.com/problems/babylonian
// =============================================================================
// Problem involving the interpretation of a string representing a base 60
// number. The value is given as a series of separated components in the 0-59
// range and the expectation is that we produce the equivalent base 10 value.
// =============================================================================

open System

let convertSingle (input : string) (exponent : int) =
    // Interpret a digit as an integer, accounting for the special zero case then
    // apply the conversion from base 60 to base 10
    match input with
        | "" -> 0L
        | _ -> int64 input
    |> (*) (pown 60L exponent)

let convertCommaSeparated (input : string) =
    // Split up the string into pieces, process each, then combine using addition
    let splits = input.Split ','
    [0..splits.Length-1]
    |> Seq.map (function x -> convertSingle splits.[x] (splits.Length - x - 1))
    |> Seq.sum

[<EntryPoint>]
let main argv =
    let cases = Console.ReadLine() |> int
    [0..cases-1]
    |> Seq.map (fun x -> Console.ReadLine())
    |> Seq.map convertCommaSeparated
    |> Seq.iter (function x -> printfn "%i" x)
    0
