# coolors-to-cavalry

A simple python script that converts a [Coolors](https://coolors.co/) palette into a [Cavalry](https://cavalry.studio/en/) compatible one.

One of Coolors' export options under 'Code' is 'Object'. This script takes that and creates a `.pal` file that can be imported in Cavalry.

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

## Usage

1. Open [`cavalry-convert.py`](https://github.com/bandinator27/coolors-to-cavalry/blob/main/cavalry-convert.py) in your favorite text editor
2. Replace `coolor_code`'s content with the coolors object
3. Edit `palette_name`
4. Save and run the script:

    ```bash
    python cavalry-convert.py
    ```

5. The created `.pal` file then can be imported in Cavalry

The script won't override an already existing file unless you type `y` when prompted.
