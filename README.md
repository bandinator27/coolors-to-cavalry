# coolors-to-cavalry

A simple python script that converts a [Coolors](https://coolors.co/) palette into a Cavalry compatible one.

One of Coolors' export options under 'Code' is 'Object'. This script takes that and creates a `.pal` file that can be imported into Cavalry.

## Example

Coolors palette:

```json
{"Punch Red":"e63946","Honeydew":"f1faee","Frosted Blue":"a8dadc"}
```

Cavalry palette `summer ocean breeze.pal`:

```json
{
    "colors": [
        {
            "color": "#e63946",
            "swatchName": "Punch Red"
        },
        {
            "color": "#f1faee",
            "swatchName": "Honeydew"
        },
        {
            "color": "#a8dadc",
            "swatchName": "Frosted Blue"
        }
    ],
    "designer": "Coolors",
    "name": "Summer Ocean Breeze",
    "version": 1.0
}
```

---

The script won't override an already existing file unless you type `y` when prompted.
