// NAME : Reversed Binary Numbers
// URL  : https://open.kattis.com/problems/reversebinary
// =============================================================================
// Simple problem to apply basic concepts of F#. Solution involves simple
// string/integer conversions and string manipulation, lending itself to a
// set of simple functions chained together in a pipeline.
// =============================================================================

open System

let toInteger s = System.Int32.Parse(s)
let toBinary (x : int) = Convert.ToString(x, 2)
let fromBinary (s : string) = Convert.ToInt32(s, 2)
let reverse (s : string) = List.ofSeq s |> List.toArray |> Array.rev |> System.String

[<EntryPoint>]
let main argv =
    Console.ReadLine()
    |> toInteger
    |> toBinary
    |> reverse
    |> fromBinary
    |> (fun i -> printfn "%i" i)
    0
