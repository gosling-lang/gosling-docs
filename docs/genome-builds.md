---
title: Genome Builds
---
You can specify genome builds through an `assembly` property (default: `"hg38"`).

```typescript
{
  "assembly": "hg38", // Globally define assembly to all tracks except ones that specify a certain assembly
  "tracks": [{
    ..., "assembly": "hg19" // Use a different assembly for this track
  }],
  ...
}
```

Gosling currently supports the following six genome builds: `hg38`, `hg19`, `hg17`, `hg16`, `mm10`, and `mm9`.